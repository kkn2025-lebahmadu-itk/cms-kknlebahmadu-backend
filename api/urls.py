from django.urls import path
from .views import admin_views

urlpatterns = [
    # admin views
    path('admin', admin_views.admin_views, name="admin-views"),
    path('admin/<int:id>', admin_views.admin_views, name="admin-views-id")
]