from fastapi import APIRouter
from cars.db.db_cars import db_cars


router = APIRouter()


fake_list_db_cars = db_cars


@router.get("/cars/", tags=["cars"])
def list_cars():
    return fake_list_db_cars
