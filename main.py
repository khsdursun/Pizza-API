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
    
    
restaurants = [
    Restaurant(
        name="La Piazza",
        address="ул. Панфилова, 12, Алматы"
    ),
    Restaurant(
        name="Sushi Master",
        address="пр. Абая, 45, Алматы"
    ),
    Restaurant(
        name="Burger House",
        address="ул. Сейфуллина, 221, Алматы"
    ),
    Restaurant(
        name="Tokyo Grill",
        address="ул. Байтурсынова, 89, Алматы"
    ),
    Restaurant(
        name="Steak & Grill",
        address="пр. Назарбаева, 32, Алматы"
    ),
    Restaurant(
        name="Khachapuri & Wine",
        address="ул. Толе би, 58, Алматы"
    ),
    Restaurant(
        name="Beshbarmak House",
        address="ул. Достык, 99, Алматы"
    ),
    Restaurant(
        name="Casa Mexicana",
        address="пр. Абылай хана, 12, Алматы"
    ),
    Restaurant(
        name="French Corner",
        address="ул. Жибек жолы, 17, Алматы"
    ),
    Restaurant(
        name="Tandoor Palace",
        address="ул. Гагарина, 130, Алматы"
    ),
    Restaurant(
        name="Pizza Familia",
        address="ул. Сатпаева, 77, Алматы"
    ),
]
