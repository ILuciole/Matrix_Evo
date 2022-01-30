from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page, name='home'),
    path('users/', views.users_base, name='users'),
]