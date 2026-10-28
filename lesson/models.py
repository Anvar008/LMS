from django.db import models

from accounts.models import Teacher
from basemanager.models import BaseManager
from education.models import Course, Group


# Create your models here.

class Modules(BaseManager):
    title = models.CharField(max_length=140)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_modules')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_modules')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_modules')

class Room(BaseManager):
    title = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number} | {self.capacity}'

class Lesson(BaseManager):
    title = models.CharField(max_length=100)
    description = models.TextField()
    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='lessons')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='lessons')

