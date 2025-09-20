from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- import this
from .database import Base, engine
from .routes import users, doctors, appointments

app = FastAPI(title="Medical Appointment Booking")

# Allow frontend to access backend
origins = [
    "http://127.0.0.1:5500",  # If you run index.html with Live Server in VS Code
    "http://localhost:5500",
    "*",  # Optional: allow all origins (for testing only)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get("/")
def root():
    return {"message": "Welcome to Medical Appointment Booking API!"}

