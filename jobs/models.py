from django.db import models
from django.utils import timezone
# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now) 

    def __str__(self):
        return self.summary 

class JobDetail(models.Model):
    title = models.CharField(max_length= 255)
    tech_used = models.CharField(max_length= 100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

