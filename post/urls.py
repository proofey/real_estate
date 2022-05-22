from django.urls import path
from . import views

urlpatterns = [
    path('post-details/<id>', views.post_details, name='post-details')
]