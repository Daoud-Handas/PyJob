from django.shortcuts import render
from django.contrib import messages

from .forms import EmailForm
from .models import Email, Job


def index(request):
    jobs = Job.objects.all()[:100]

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

    return render(request, "Jobs/index.html", context={'jobs': jobs, "form":form})


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

