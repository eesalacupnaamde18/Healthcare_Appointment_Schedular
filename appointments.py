from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=schemas.Appointment)
def book_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(database.get_db)):
    return crud.appointment_crud.create_appointment(db, appointment)

@router.get("/{user_id}", response_model=list[schemas.Appointment])
def list_appointments(user_id: int, db: Session = Depends(database.get_db)):
    return crud.appointment_crud.get_appointments(db, user_id)
