from django.urls import path, include
from . import views

app_name="webiste"
urlpatterns = [
    path('', views.get_list, name="home"),
    path('home', views.get_list, name="home"),
    path('details', views.get_details, name="details"),

]
