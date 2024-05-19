from django.db import models

class Job(models.Model):
  email = models.EmailField()
  title = models.TextField(max_length=30)
  description = models.TextField()
  min_pay = models.IntegerField()
  date = models.DateField(default=None, null=True, blank=True)  
