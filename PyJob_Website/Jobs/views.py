from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib import messages

from .forms import EmailForm


def index(request):
    return HttpResponse("Hello, world. You're at the Jobs index.")


def email(request):

    # if form submitted
    if request.method == 'POST':
        # get form with fields filed by request
        form = EmailForm(request.POST)
        if form.is_valid():
            messages.success(request, f"Email successfully recorded : {form.cleaned_data['your_email']}")
        else:
            messages.error(request, f"Email unsuccessfully recorded :(")
    else:
        form = EmailForm()
    return render(request, 'Jobs/email.html', {'form': form})
