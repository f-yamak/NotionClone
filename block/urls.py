from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.homepage, name='homepage'),
    path("index/",views.index ,name="index"),
    path('add_page/', views.add_page, name='add_page'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('search/', views.search, name='search'),
    path('inbox/', views.inbox, name='inbox'),
    path('members_settings/', views.members_settings, name='members_settings'),
    path('calendar/', views.calendar, name='calendar'),
    path('templates/', views.templates, name='templates'),
    path('help_supports/', views.help_supports, name='help_supports'),
    path('trash/', views.trash, name='trash'),
    path('birthday/', views.birthday, name='birthday'),
    path('todo/', views.todo, name='todo'),
    path('movie/', views.movie, name='movie'),
    path('event/', views.event, name='event'),
    path('shopping/', views.shopping, name='shopping'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    


    ]

