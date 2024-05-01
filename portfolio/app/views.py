from django.shortcuts import render
from django.views.generic import ListView
from .models import Banner, Service, Feature, About, Contact

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


