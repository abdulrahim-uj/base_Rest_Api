from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=128)
    task_desc = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='Images/', default="Images/None/Noimg.jpg")
