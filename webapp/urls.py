from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('property/', views.property, name = 'property'),
    path('homeloan/', views.homeloan, name = 'homeloan'),
    path('personalloan/', views.personalloan, name = 'personalloan'),
    path('businessloan/', views.businessloan, name = 'businessloan'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('vehicle/', views.vehicle, name = 'vehicle'),
    path('consulting/', views.consulting, name = 'consulting'),

]