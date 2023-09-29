from django.urls import path
from .views import UserListCreateView, EventListCreateView, InvitationListCreateView, AcceptInvitationView, \
    SendInvitationView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('invitations/', InvitationListCreateView.as_view(), name='invitation-list-create'),
    path('invitations/<int:pk>/accept/', AcceptInvitationView.as_view(), name='accept-invitation'),
    path('invitations/send/', SendInvitationView.as_view(), name='send-invitation'),

]
