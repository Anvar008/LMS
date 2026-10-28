from django.contrib.auth.models import AbstractUser
from django.db import models

from basemanager.models import BaseManager


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('visitor', 'Visitor'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='visitor')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Teacher(BaseManager):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    experience = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/teachers/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Student(BaseManager):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    study_place = models.CharField(blank=True, null=True)
    address = models.CharField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/students/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
