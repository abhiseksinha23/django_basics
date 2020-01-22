from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=259)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=234)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})
class Student(models.Model):
    name = models.CharField(max_length=230)
    age = models.PositiveIntegerField()
    school =models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
