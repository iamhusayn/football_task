from django.db import models

# Create your models here.
class TaskModel(models.Model):
  # user =models.OneToOneField('users.user', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to="media")
  deadline = models.DateField()