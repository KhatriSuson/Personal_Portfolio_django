from django.urls import path
from .views import *

urlpatterns = [
    # path("", BannerView.as_view(), name="home"),
    path("", home, name="home"),
    # path('about/', about, name='about'),
    path("about/", AboutView.as_view(), name="about"),
    path("service/", ServiceView.as_view(), name="service"),
    path("feature/", FeatureView.as_view(), name="feature"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("login/", login, name="login"),
    path("signup/", singup, name="singup"),






    # path('login/', LoginView.as_view(), name="login"),
]
