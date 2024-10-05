from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Circle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='circles')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name