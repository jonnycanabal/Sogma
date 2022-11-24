from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# from celery.decorators import task
# from celery.task.schedules import crontab
from celery.schedules import crontab
from main.celery import app

@app.add_periodic_task(
run_every=(app.task.schedules.crontab(hour=17, minute=2)), #runs exactly at 3:34am every day
name="Dispatch_scheduled_mail",
reject_on_worker_lost=True,
ignore_result=True)
def schedule_mail():
    message = render_to_string('gestionActivos/emailAlarma.html')
    mail_subject = 'Scheduled Email'
    to_email = 'jonny.canabal@gmail.com'
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()