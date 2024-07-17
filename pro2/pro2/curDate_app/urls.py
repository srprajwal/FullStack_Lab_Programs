from django.urls import path
from curDate_app import views

urlpatterns = [
    path('ahead4/',views.ahead4),
    path('behind4/',views.behind4),
]