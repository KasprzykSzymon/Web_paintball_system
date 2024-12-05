from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    participants = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.field.name} ({self.date} {self.time})"