from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel


app = FastAPI()


class Restaurant(BaseModel):
    name: str
    address: str
    
class Chef(BaseModel):
    name: str
    restaurant_id = int
    
class Pizza(BaseModel):
    name: str
    cheese: str
    dough: str
    secret_ingredient = str

class Ingredient(BaseModel):
    name: List[str]
    
class Review(BaseModel):
    restaurant: str
    rating: int
    text: str
    