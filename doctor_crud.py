from sqlalchemy.orm import Session
from .. import models, schemas

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(name=doctor.name, specialty=doctor.specialty)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Doctor).offset(skip).limit(limit).all()
