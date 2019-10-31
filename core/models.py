from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Slimeline(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=128, default="SLIMELINE NAME UNKNOWN")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="slimeline_owner", default="NULL")

    def __str__(self):
        return self.name + " by " + self.owner.first_name

class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_author", default="NULL")
    slimeline = models.ForeignKey(Slimeline, related_name="events", on_delete=models.CASCADE, default=0)
    
    title = models.CharField(max_length=128, default="TITLE UNKNOWN")
    summary = models.CharField(max_length=128, default="SUMMARY UNKNOWN")
    content = models.TextField(default="")
    is_private = models.BooleanField(default=False) # visible to creator only
    good_slimes = models.IntegerField(default=0) # equivalent of "like" button
    
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    
    
    def __str__(self):
        return self.author.username + " posted : " + self.title