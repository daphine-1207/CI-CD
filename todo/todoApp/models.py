from django.db import models

# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

def __str__ (self):
    return self.task