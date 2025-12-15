import os
from datetime import datetime, timedelta, timezone
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import SQLModel, Field, Session, select, create_engine
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# --- CONFIG ---
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_on_production")
SYSTEM_ADMIN_USERNAME = os.getenv("SYSTEM_ADMIN_USERNAME")
SYSTEM_ADMIN_PASSWORD = os.getenv("SYSTEM_ADMIN_PASSWORD")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SQLITE_FILE_NAME = "production_app.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

# --- SECURITY SETUP ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SYSTEM_ADMIN_PASSWORD_HASH = pwd_context.hash(SYSTEM_ADMIN_PASSWORD)

# --- DATABASE MODELS ---

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    email: Optional[str] = None
    role: str = "user"  # Default role is 'user'

class UserCreate(BaseModel):
    # Used for Registration Request Body
    username: str
    password: str
    email: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

# --- DB ENGINE ---
engine = create_engine(SQLITE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# --- SECURITY UTILS ---

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- DEPENDENCIES (The Gatekeepers) ---

# 1. Get the Current User (Authentication)
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # --- SYSTEM ADMIN ---
    if username == SYSTEM_ADMIN_USERNAME:
        return User(
            id=0,
            username=SYSTEM_ADMIN_USERNAME,
            email=None,
            role="admin",
            hashed_password=""
        )

    # --- NORMAL USER ---
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise credentials_exception

    return user


# 2. Get Admin Only (Authorization)
async def get_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403, 
            detail="Forbidden: You do not have admin privileges"
        )
    return current_user

# --- API APP ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Startup")
    create_db_and_tables()
    yield
    # Shutdown
    print("Shutdown")

app = FastAPI(lifespan=lifespan)
# --- ROUTES ---

# 1. REGISTER (Anyone can create an account)
@app.post("/register", response_model=Token)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    # Check if user exists
    statement = select(User).where(User.username == user_data.username)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Create DB Object
    role = "admin" if user_data.username.lower() == "admin" else "user"
    
    db_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        role=role
    )
    
    session.add(db_user)
    session.commit()
    
    # Auto-login after register
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 2. LOGIN (Get Token)
@app.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    # --- SYSTEM ADMIN LOGIN ---
    if form_data.username == SYSTEM_ADMIN_USERNAME:
        if not pwd_context.verify(form_data.password, SYSTEM_ADMIN_PASSWORD_HASH):
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        access_token = create_access_token(
            data={"sub": SYSTEM_ADMIN_USERNAME, "role": "admin"}
        )
        return {"access_token": access_token, "token_type": "bearer"}

    # --- NORMAL USER LOGIN ---
    statement = select(User).where(User.username == form_data.username)
    user = session.exec(statement).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 3. GET MY PROFILE (Any Logged-in User)
@app.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
        "status": "Active"
    }

# 4. ADMIN ONLY ENDPOINT
# Try accessing this with a normal user -> 403 Error
@app.get("/admin/users", dependencies=[Depends(get_admin_user)])
def read_all_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users