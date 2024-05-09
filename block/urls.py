from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage ,name="homepage"),
    path("index/",views.index ,name="index"),
    path('', views.anasayfa, name='anasayfa'),
    path('add_page/', views.add_page, name='add_page'),
    path('tasks/', views.gorevler, name='gorevler'),
    path('search/', views.search, name='search'),
    path('inbox/', views.inbox, name='inbox'),
    path('members_settings/', views.members_settings, name='members_settings'),
    path('calendar/', views.calendar, name='calendar'),
    path('templates/', views.templates, name='templates'),
    path('help_supports/', views.help_supports, name='help_supports'),
    path('trash/', views.trash, name='trash'),


    ]

