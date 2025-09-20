from sqlalchemy.orm import Session
from .. import models, schemas

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(
        user_id=appointment.user_id,
        doctor_id=appointment.doctor_id,
        appointment_time=appointment.appointment_time
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session, user_id: int):
    return db.query(models.Appointment).filter(models.Appointment.user_id == user_id).all()
