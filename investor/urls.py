from django.conf import settings
from django.urls import path, include
from . import views

from django.conf.urls.static import static

app_name = 'investor'

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.registerlogin, name='login'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('content', views.content, name='content'),
    path('details/<str:ideaname>', views.details, name='details'),
    path('appointment/<str:enpmail>', views.appointment, name='appointment'),
    path('ignore/<str:enpmail>', views.ignore, name='ignore'),
    path('successful', views.successful, name='successful'),
    path('profile', views.profile, name='profile'),
    path('idealike',views.idealike,name='idealike'),
]
