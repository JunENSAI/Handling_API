from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select
from contextlib import asynccontextmanager

# --- 1. SETUP DATABASE ---
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    """Creates the tables if they don't exist."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency: Provides a DB session and closes it after request."""
    with Session(engine) as session:
        yield session

# --- 2. DEFINE MODEL ---
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True) # index=True makes searching faster
    secret_name: str
    age: Optional[int] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Startup")
    create_db_and_tables()
    yield
    # Shutdown
    print("Shutdown")

app = FastAPI(lifespan=lifespan)

# --- CREATE ---
@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero) 
    return hero

# --- READ ALL ---
@app.get("/heroes/", response_model=List[Hero])
def read_heroes(session: Session = Depends(get_session)):
    statement = select(Hero)
    heroes = session.exec(statement).all()
    return heroes

# --- READ ONE ---
@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
