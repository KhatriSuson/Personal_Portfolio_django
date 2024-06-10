from django.contrib import admin

# from .models import Banner, Service, Feature, About, Contact
from .models import *


# Register your models here.
admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(MyContact)

admin.site.register(SocialMedia)
admin.site.register(Info)
admin.site.register(Team)
admin.site.register(Feedback)
