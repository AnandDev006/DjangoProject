from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    complete = models.BooleanField( default = False)
    todoText = models.CharField( max_length = 50)
    created_at = models.DateTimeField( default = timezone.now())
    
    def __str__(self):
        return self.todoText