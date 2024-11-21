from django.urls import path
from . import views

# list of all urls that are defined in the blog app that will be connected to html pages/views

urlpatterns = [
    # home page
    path('', views.post_list, name='post_list'),
]