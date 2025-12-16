from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# 1. APP METADATA
description_text = """
**The Marvel Superhero API** helps you manage your hero roster.

## Features
* **Create** new heroes with power stats.
* **Search** for heroes by team.
* **Secure** endpoints (Coming soon).

## Contact
* Manager: Nick Fury (nick@shield.gov)
"""

app = FastAPI(
    title="Marvel SuperHero API",
    description=description_text,
    version="2.5.0",
    terms_of_service="http://example.com/terms/", # link does not have to be real for now
    contact={
        "name": "S.H.I.E.L.D. Support",
        "url": "http://example.com/contact/",
        "email": "donttryemailthis@gmail.com", # use a real email in production, for now it's just an example
    },
    license_info={
        "name": "Top Secret License",
        "url": "http://example.com/license/",
    },
)

# 2. MODELS WITH EXAMPLES
class Hero(BaseModel):
    name: str = Field(..., example="Iron Man", description="The hero's public name")
    secret_identity: str = Field(..., example="Tony Stark", description="Real name (Classified)")
    power_level: int = Field(
        default=50, 
        ge=0, 
        le=100, 
        description="Power rating from 0 to 100",
        example=95
    )
    tags: list[str] = Field(default=[], example=["rich", "armor", "flying"])

# 3. TAGS (Grouping) : Without tags, all endpoints are mixed together. Tags create sections.
TAG_HEROES = "Heroes Management"
TAG_META = "System Info"

@app.post(
    "/heroes/", 
    response_model=Hero, 
    status_code=status.HTTP_201_CREATED,
    tags=[TAG_HEROES],
    summary="Recruit a new Hero", # Short title
    description="Adds a hero to the active roster. **Requires Level 5 Clearance**." # Long description (supports Markdown)
)
def create_hero(hero: Hero):
    """
    You can also write the description here (Docstring).
    FastAPI will read this text and put it in the docs 
    if you don't use the 'description' parameter above.
    """
    return hero

@app.get(
    "/heroes/{name}", 
    tags=[TAG_HEROES],
    summary="Find Hero Details",
    # 4. CUSTOM RESPONSES
    responses={
        404: {"description": "Hero went rogue or was not found"},
        200: {
            "description": "Hero dossier found successfully",
            "content": {
                "application/json": {
                    "example": {"name": "Thor", "secret_identity": "Thor Odinson", "power_level": 100}
                }
            }
        }
    }
)
def read_hero(name: str):
    if name == "Thanos":
        raise HTTPException(status_code=404, detail="Thanos is a villain, not a hero.")
    return {"name": name, "secret_identity": "Who?", "power_level": 80}

@app.get("/health", tags=[TAG_META])
def health_check():
    return {"status": "Operational"}