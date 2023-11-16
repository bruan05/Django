from django.urls import path

from mysite.urls import views

urlpatterns = [
    path("polls/", views.index, name="index"),
]