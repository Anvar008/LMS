from django.db import models

# Create your models here.

class NewsCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class New(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.date}'
