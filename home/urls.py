from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_homepage, name='home'),
    path('menu', views.show_menu, name='menu'),
    path('new_music', views.show_new_music, name='new_music'),
    path('sotw', views.show_sotw, name='sotw'),
    path('about', views.show_about, name='about'),
]