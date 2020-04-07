from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse

# Create your views here.


def index(request):

    return render(request, 'prva/index.html')


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    else:
        form = ContactForm()

        return render(request, 'prva/contact.html', {"form": form})
