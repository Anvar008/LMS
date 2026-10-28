from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('courses/', course, name='courses'),
    path('course/category/add/', add_course_category, name='add_course_category'),
    path('course/add/', add_course, name='add_course'),
    path('course/<int:pk>/detail/', course_detail, name='course_detail'),
    path('group/', group, name='group'),
    path('group/add_group/', add_group, name='add_group'),
    path('group/add_student/<str:group_id>/', add_group_student, name='add_group_student'),
    path('group/edit/<int:pk>/', group_edit, name='group_edit'),
]
