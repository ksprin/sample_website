from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("aboutme", views.skills, name= 'skills'),
    path("whyigem", views.right, name = 'right'),
]