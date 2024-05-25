from django.db import models

class TodoItem(models.Model):
    name = models.CharField(max_length=50)
    creation_time_stamp = models.DateTimeField(auto_now_add=True)
    

 
