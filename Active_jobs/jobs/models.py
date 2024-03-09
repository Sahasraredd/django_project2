from django.db import models

# Create your models here.
class job(models.Model):
    eno = models.IntegerField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    skills = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return 'job object with eno:+str(self.eno)'