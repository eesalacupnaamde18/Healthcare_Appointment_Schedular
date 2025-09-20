from pydantic import BaseModel, EmailStr
from datetime import datetime

# Users
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# Doctors
class DoctorBase(BaseModel):
    name: str
    specialty: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    class Config:
        orm_mode = True

# Appointments
class AppointmentBase(BaseModel):
    doctor_id: int
    appointment_time: datetime

class AppointmentCreate(AppointmentBase):
    user_id: int

class Appointment(AppointmentBase):
    id: int
    status: str
    class Config:
        orm_mode = True
