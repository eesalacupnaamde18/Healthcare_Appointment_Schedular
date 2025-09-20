from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/doctors", tags=["doctors"])

@router.get("/", response_model=list[schemas.Doctor])
def list_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.doctor_crud.get_doctors(db, skip, limit)

@router.post("/", response_model=schemas.Doctor)
def add_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(database.get_db)):
    return crud.doctor_crud.create_doctor(db, doctor)
