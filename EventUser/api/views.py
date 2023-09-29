from django.contrib.auth.models import User
from .models import Event, Invitation
from .serializers import UserSerializer, EventSerializer, InvitationSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(Q(creator=user) | Q(collaborators=user)).distinct()


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class InvitationListCreateView(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class AcceptInvitationView(generics.UpdateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.invited_user != request.user:
            return Response({'error': 'You do not have permission to accept this invitation.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Invitation accepted'}, status=status.HTTP_200_OK)


class SendInvitationView(generics.CreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
