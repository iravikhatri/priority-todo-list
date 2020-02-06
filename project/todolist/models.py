from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):

    CHOICES = (
        ("low", 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )

    title = models.CharField(max_length=100)
    task = models.TextField()
    status = models.BooleanField(default=False, null=True)
    priority = models.CharField(max_length=10 ,choices=CHOICES, default="medium")
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
