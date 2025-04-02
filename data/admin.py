from django.contrib import admin
from .models import User, News, Complaint

# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Complaint)