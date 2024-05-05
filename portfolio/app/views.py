from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import *
from django.urls import reverse

# Banner, Service, Feature, About, Contact

# Create your views here.


# class BannerView(ListView):
#     model = Banner
#     template_name = 'index.html'
#     context_object_name = 'banners'


def home(request):
    views = {}
    views["services"] = Service.objects.all()
    views["banners"] = Banner.objects.all()
    views["features"] = Feature.objects.all()
    views["medias"] = SocialMedia.objects.all()

    return render(request, "index.html", views)


# def about(request):
#         views = {}
#         views['abouts'] = About.objects.all()
#         return render (request, 'about.html', views)


class AboutView(ListView):
    model = About
    template_name = "about.html"
    context_object_name = "abouts"


class ServiceView(ListView):
    model = Service
    template_name = "service.html"
    context_object_name = "services"


class FeatureView(ListView):
    model = Feature
    template_name = "feature.html"
    context_object_name = "features"


# class ContactView(ListView):
#     model = Contact
#     template_name = 'contact.html'
#     context_object_name = "contacts"


def contact_form(request):
    if request.method == "POST":
        contact = MyContact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        # return HttpResponse("<h1> THANKS FOR CONTACT </h1>")
        # return render(request, "hello.html")
    return render(request, "contact.html")


## user auth


def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, "Invalid Username")
            return redirect("/home/")

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect("/login/")

    # Render the login page template (GET request)
    return render(request, "user/login.html")


# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect("user/register/")

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect("/register/")

    # Render the registration page template (GET

    return render(request, "user/register.html")
