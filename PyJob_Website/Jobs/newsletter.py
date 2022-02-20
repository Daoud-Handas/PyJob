from django.utils import timezone

from .models import Job, Email


def get_last_week_jobs():
    # TODO change to days=1 for last days
    previous_date = timezone.now() - timezone.timedelta(days=5)
    return Job.objects.filter(date_added__gte=previous_date)


