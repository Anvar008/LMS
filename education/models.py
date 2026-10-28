from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import Teacher, Student
from basemanager.models import BaseManager


# Create your models here.

class CourseCategory(BaseManager):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Course(BaseManager):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/')
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.title} | {self.price} | {self.duration}'

class Group(BaseManager):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_group')
    students = models.ManyToManyField(Student, related_name='student_group', blank=True)
    title = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    max_students = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    start_time = models.CharField(max_length=10)
    finish_time = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} | {self.course}'
