from django.urls import path

from . import views

urlpatterns = [
    path("background/", views.background, name="index"),
    path("email/", views.email, name="index"),
    path("mtknr/", views.mtknr, name="index"),
    path("name/", views.name, name="index"),
    path("programOfStudy/", views.programOfStudy, name="index"),
    path("skills/", views.skills, name="index"),
    path("topics/", views.topics, name="index")
]
