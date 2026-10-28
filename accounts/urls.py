from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('add/user/', add_user, name='add_user'),
    path('profile/teacher/', teacher_profile, name='teacher_profile'),
    path('profile/student/', student_profile, name='student_profile'),
]