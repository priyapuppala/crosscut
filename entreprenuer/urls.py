
from django.urls import path, include
from . import views

app_name = 'entreprenuer'

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.registerlogin, name='login'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('content', views.content, name='content'),
    path('details/<str:mail>', views.details, name='details'),
    path('successful', views.successful, name='successful'),
    path('ideas/<str:mail>', views.idea, name='idea'),
]