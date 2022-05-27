from django.urls import path
from . import views

urlpatterns = [
    path('post-details/<id>', views.post_details, name='post-details'),
    path('new-post', views.new_post, name='new-post'),
    path('delete-post/<id>', views.delete_post, name='delete-post')
]