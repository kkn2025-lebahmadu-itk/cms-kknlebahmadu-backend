from django.contrib import admin
from .models import User, News, Complaint, Profile, Gallery

# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Complaint)
admin.site.register(Profile)
admin.site.register(Gallery)