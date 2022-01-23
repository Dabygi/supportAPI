from supportAPI.celery import app
from authorization.service import send


@app.task
def send_activation_email(user_email):
    send(user_email)