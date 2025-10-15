from django.contrib import messages
from .models import About, Skill, Project, Experience, Education, ContactMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from .forms import ContactForm
from django.conf import settings

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    context = {
        "about": about,
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "educations": educations,
    }

    if request.method == "POST":
        print("POST request received")
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ["didingangadharpg@gmail.com"], # change to where you want to receive emails
            fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            # return redirect("home")

    return render(request, "index.html", context)

def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        messages.success(request, "Your message has been sent!")
    return redirect("home")

def online_shop(request):
    return render(request, 'online-shop.html')

def health_stack(request):
    return render(request, 'health_stack.html')

def classmanager(request):
    return render(request, 'classmanager.html') 

def lapzone(request):
    return render(request, 'lapzone.html')

def gym(request):
    return render(request, 'gym.html')

def train_food(request):
    return render(request, 'train_food.html')

def Hotel_room(request):
    return render(request, 'Hotel_room.html')

def job_portal(request):
    return render(request, 'job_portal.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# views.py (improved version with error handling)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ["didingangadharpg@gmail.com"], # change to where you want to receive emails
            fail_silently=False,
            )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")
    else:
        form = ContactForm()

    return render(request, "index.html", {"form": form})