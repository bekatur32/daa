from . import views
from django.urls import path
urlpatterns = [
    path('',views.ttt)
    path('Home_page',views.home_page),
    path('About_page',views.about_page),
    path('news', views.news),
    path('contacts',views.contacts)
]