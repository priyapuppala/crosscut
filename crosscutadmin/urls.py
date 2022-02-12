
from django.urls import path
from . import views

app_name = 'crosscutadmin'


urlpatterns = [
    path("", views.homefunction, name="home"),
    path("home", views.homefunction, name="home"),
    path("services", views.servicesfunction, name="services"),
    path("about", views.aboutfunction, name="about"),
    path("logout",views.logout, name="logout"),

    path("invdet", views.invdetfunction, name="invdet"),
    path("enpdet",views.enpdetfunction, name="enpdet"),
    path("invqr",views.invqrfunction, name="invqr"),
    path("enpqr",views.enpqrfunction, name="enpqr"),
    path("dashboard",views.dashboard, name="dashboard"),

    path("ereply/<str:subject>", views.ereplyfunction, name="ereply"),
    path("edelete/<str:subject>", views.edeletefunction, name="edelete"),
    path("ireply/<str:subject>", views.ireplyfunction, name="ireply"),
    path("idelete/<str:subject>", views.ideletefunction, name="idelete"),

    path("indelete/<str:email>", views.indeletefunction, name="indelete"),
    path("epdelete/<str:email>", views.epdeletefunction, name="epdelete"),

    path("ereplymail/<str:subject>", views.ereplymailfunction, name="ereplymail"),
    path("ireplymail/<str:subject>", views.ireplymailfunction, name="ireplymail"),
]