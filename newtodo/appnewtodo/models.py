from django.db import models

# Create your models here.
class Todo_data(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    date = models.DateField()


