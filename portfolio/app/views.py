from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, View
from .models import Banner, Service, Feature, About, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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


class ContactView(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = "contacts"


# def login(request):
    
#         return render(request, "authentication/login.html")


def login(request):
    
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            users = authenticate(request, username=username, password=password)
            if users is not None:
                login(request, users)
                return redirect('home')
            else:
                messages.susccess(request, ("The is error Establish"))
                return redirect('login')
    else:

        return render(request, "registration/login.html")

def singup(request):
    return render(request, "testsignup.html")












# def login(request):
    # return render(request, "account/login.html")

# class LoginView(View):
#     template_name = 'testlogin.html'
#     context_objects_name = 'logins'
# def login(request):
#     return render(request, "testlogin.html")



