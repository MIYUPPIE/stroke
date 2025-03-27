from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_stroke, name='predict_stroke'),
    path('register/', views.register, name='register'),
    path('profile_setup/', views.profile_setup, name='profile_setup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
