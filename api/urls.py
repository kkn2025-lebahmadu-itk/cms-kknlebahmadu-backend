from django.urls import path
from .views import admin_views, news_views, complaint_views, profile_views, gallery_views, home_views, report_views, recap_views

urlpatterns = [
    # ADMIN VIEWS
    path('admin', admin_views.admin_views, name="admin-views"),
    path('admin/<int:id>', admin_views.admin_views, name="admin-views-id"),

    # NEWS VIEWS
    # TODO : Create the better urls
    path('news', news_views.news_views, name="news-views"),
    path('news/<slug:slug>', news_views.news_views, name="news-views-id"),


    
    # COMPLAINT VIEWS
    path('complaint', complaint_views.complain_views, name='complain-views'),
    path('complaint/<int:id>', complaint_views.complain_views, name='complain-views-id'),

    # PROFILE VIEWS
    path('profile', profile_views.profile_views, name='profile-views'),
    path('profile/<int:id>', profile_views.profile_views, name='profile-views-id'),


    # GALLERY VIEWS
    path('gallery', gallery_views.gallery_views, name='gallery-views'),
    path('gallery/<int:id>', gallery_views.gallery_views, name='gallery-views-id'),

    # REPORT VIEWS
    path('report', report_views.report_views, name='report-views'),
    path('report/<int:id>', report_views.report_views, name='report-views-id'),

    # RECAP VIEWS
    path('recap', recap_views.recap_views, name='recap-views'),
    path('recap/<int:id>', recap_views.recap_views, name='recap-views-id'),

    
    # HOME VIEWS
    path('home', home_views.home_views, name='home-views'),
]