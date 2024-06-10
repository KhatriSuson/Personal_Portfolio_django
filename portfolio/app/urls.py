from django.urls import path
from app.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import reverse

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("service/", ServiceView.as_view(), name="service"),
    path("feature/", FeatureView.as_view(), name="feature"),
    path('team/', TeamView.as_view(), name='team'),
    path("contact/", contact_form, name="contact"),
    
    
    # user auth
    path("login/", login_page, name="login_page"),  # Login page
    path("register/", register_page, name="register"),  # Registration page
    # login_url = reverse('login')
] 


# # Serve media files if DEBUG is True (development mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Serve static files using staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()
