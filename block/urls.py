from django.urls import path
from . import views

urlpatterns = [
        path("",views.homepage ,name="homepage"),
        path("index/",views.index ,name="index"),
    ]

