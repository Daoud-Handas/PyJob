from django.http import HttpResponse
from .indeed import *
from .models import Job
from django.shortcuts import render
from django.contrib import messages

from .forms import EmailForm
from .models import Email


def index(request):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format('data scientist', 'Paris')
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'job_seen_beacon')

    #jobs = Job.objects.all()[:15]

def email(request):

    # if form submitted
    if request.method == 'POST':
        # get form with fields filed by request
        form = EmailForm(request.POST)
        if form.is_valid():
            email_record = Email(email=form.cleaned_data['your_email'])
            try:
                email_record.name = form.cleaned_data["your_name"]
            except NameError:
                pass
            email_record.save()
            messages.success(request, f"Email successfully recorded : {form.cleaned_data['your_email']}")
        else:
            messages.error(request, f"Email unsuccessfully recorded :(")
    else:
        form = EmailForm()
    return render(request, 'Jobs/email.html', {'form': form})

    return render(request, "index.html", context={'jobs': jobs})