from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('administrator', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('search/', views.search_request, name='search')
]