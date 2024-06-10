from django.urls import path
from . import views



urlpatterns = [
    path('', views.home ,name='home'),
    path('api/student_list/', views.student_list, name='student'),
    path('api/student_detail/<int:pk>/', views.student_detail, name='student_detail'),
    
]