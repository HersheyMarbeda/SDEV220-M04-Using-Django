from django.urls import path
from . import views

# list of all urls that are defined in the blog app that will be connected to html pages/views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]