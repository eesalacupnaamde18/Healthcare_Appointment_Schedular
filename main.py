from fastapi import FastAPI
from .database import Base, engine
from .routes import users, doctors, appointments

app = FastAPI(title="Medical Appointment Booking")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Medical Appointment Booking API!"}
