# this file is created by you, call is urls.py within the app you are in to map urls to function.
# calls, you then need to modify the views py in the parent folder
from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.janurary),
    # path("february", views.february), int before str
    path("", views.index, name="index"), #triggers /challenges
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
