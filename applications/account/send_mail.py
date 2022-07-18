from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail('Активация аккаунта', full_link, 'csqvsr25@gmail.com', [email])