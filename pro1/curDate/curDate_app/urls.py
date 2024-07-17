from django.urls import path
from curDate_app import views

urlpatterns = [
    path('date/',views.currDate),
]