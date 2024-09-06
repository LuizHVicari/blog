from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', views.post, name='post'),
    path('', views.get_post_list, name='post-list'),
    # path('projects/', views, name='list-projects'),
    # path('academic/', views, name='list-academic'),
]
