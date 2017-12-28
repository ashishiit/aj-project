'''
Created on Dec 21, 2017

@author: S528358
'''
# from django.contrib import admin
from django.urls import path, re_path
from posts import views
urlpatterns = [
#     path('admin/', admin.site.urls),
    path('', views.posts_home, name='posts_home'),
    path('create', views.posts_create, name='posts_create'),
    re_path('(?P<id_num>\d+)/$', views.posts_detail, name='posts_detail'),
    path('list', views.posts_list, name='posts_list'),
    re_path('(?P<id_num>\d+)/edit/$', views.posts_update, name='posts_update'),
    re_path('(?P<id_num>\d+)/delete/$', views.posts_delete, name='posts_delete'),
    path('', views.posts_home, name='posts_home'),
#     path('posts/', 'views.posts.posts_home', name='posts_home'),
]
