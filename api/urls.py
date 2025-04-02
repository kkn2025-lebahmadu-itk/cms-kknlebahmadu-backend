from django.urls import path
from .views import admin_views, news_views, complaint_views, profile_views

urlpatterns = [
    # ADMIN VIEWS
    path('admin', admin_views.admin_views, name="admin-views"),
    path('admin/<int:id>', admin_views.admin_views, name="admin-views-id"),

    # NEWS VIEWS
    # TODO : Create the better urls
    # path('news', news_views.news_handler, name="news-views"),
    # path('news/<int:id>', news_views.news_handler, name="news-views-id")
    path('create-news', news_views.create_news, name="create-news"), #create news.
    path('get-news', news_views.get_news, name="news-views"), # get all news
    path('get-news/<int:id>', news_views.get_news, name="news-views-id"), # get single news
    path('update-news/<int:id>', news_views.update_news, name='update-news'), # update news.
    path('delete-news/<int:id>', news_views.delete_news, name='delete-news'), # delete news.


    
    # COMPLAINT VIEWS
    path('complaint', complaint_views.complain_views, name='complain-views'),
    path('complaint/<int:id>', complaint_views.complain_views, name='complain-views-id'),

    # PROFILE VIEWS
    path('profile', profile_views.profile_views, name='profile-views'),
    path('profile/<int:id>', profile_views.profile_views, name='profile-views-id'),
]