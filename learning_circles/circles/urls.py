from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_circle, name='create_circle'),
    path('join/<int:circle_id>/', views.join_circle, name='join_circle'),
    path('exit/<int:circle_id>/', views.leave_circle, name='leave_circle'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]