from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    collaborators = models.ManyToManyField(User, related_name='collaborating_events', blank=True)

    def __str__(self):
        return self.title


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='invitations')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Invitation for {self.event.title} to {self.invited_user.username}'

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='invitations')
