from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    name = models.CharField(max_length=50)
    creation_time_stamp = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

 
