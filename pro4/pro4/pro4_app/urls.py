from django.urls import path
from pro4_app import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]