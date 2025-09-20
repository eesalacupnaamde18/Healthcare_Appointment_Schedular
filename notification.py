from celery import Celery

celery = Celery(__name__, broker="redis://localhost:6379/0")

@celery.task
def send_notification(email: str, message: str):
    print(f"Sending notification to {email}: {message}")
    # integrate email sending logic here
