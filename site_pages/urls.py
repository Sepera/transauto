from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('404', views.notfound, name='calculator'),
    path('404', views.notfound, name='404'),

]