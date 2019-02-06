from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['POST'])
def RegisterNumber(request):
    # get user phone number
    # generate a new number and send to user sms service
    # save number in user table in (pre-active phase)
    # return successfull status
    return Response('ok')


@api_view(['POST'])
def ValidateNumber(request):
    # get number from user
    # check against saved number in models
    # activate user and authenticate
    # generate new JWT token and return it

    return Response('token:123')


def GetToken(user):
    token = '123'
    return token

