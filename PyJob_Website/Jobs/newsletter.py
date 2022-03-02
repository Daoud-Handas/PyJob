from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils import timezone

from .models import Job, Email


def get_last_week_jobs():
    # TODO change to days=1 for last days
    previous_date = timezone.now() - timezone.timedelta(days=1)
    return Job.objects.filter(date_added__lte=previous_date)[:10]


def send_newsletter():
    subject = "PyJob newsletter !"
    html_template = get_template("Jobs/newsletter.html")
    jobs = get_last_week_jobs()

    emails = Email.objects.all()

    for email in emails:
        html_content = html_template.render({"jobs": jobs, "user": email.name})
        mail = EmailMessage(subject, html_content, to=[email.email])
        mail.content_subtype = "html"
        mail.send()
