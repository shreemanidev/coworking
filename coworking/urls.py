from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('index-2/', views.index),
    path('index-3/', views.homedemo),
    path('about/', views.about),
    path('workspaces/', views.workspaces),
    path('events/', views.events),
    path('events-booking/', views.eventsbooking),
    path('events-details/', views.eventsdetails),
    path('services/', views.services),
    path('services-details', views.servicesdetails),
    path('features', views.features),
    path('team', views.team),
    path('pricing', views.pricing),
    path('gallery', views.gallery),
    path('faq', views.faq),
    path('login', views.login),
    path('register', views.register),
    path('privacy-policy', views.privacypolicy),
    path('terms-of-service', views.termsofservice),
    path('error-404', views.error404),
    path('coming-soon', views.comingsoon),
    path('blog/', views.blog),
    path('blog-right-sidebar/', views.blogrightsidebar),
    path('blog-details/', views.blogdetails),
    path('contact/', views.contact)
] 
