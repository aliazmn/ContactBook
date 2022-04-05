from celery import shared_task
from django.core.mail import send_mail
from contactbook import settings

@shared_task(name ="send_email")
def send_email( email  , content  ):
    send_mail("mail_subject", content, settings.EMAIL_HOST_USER, [email])
   