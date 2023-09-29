from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, Invitation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','username','title', 'description', 'creator', 'collaborators')


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'event', 'invited_user', 'accepted')

    def validate_event(self, event):

        try:
            event = Event.objects.get(pk=1)
        except Event.DoesNotExist:
            raise serializers.ValidationError("Event does not exist")

        return event


class AcceptInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'accepted')

    def validate_accepted(self, accepted):
        if accepted is not True:
            raise serializers.ValidationError("Invitation must be accepted.")
        return accepted
