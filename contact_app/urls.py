from django.urls import path

from . import views

urlpatterns = [
    path('contact_detail', views.contact, name="contact_detail"),
]