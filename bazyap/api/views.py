from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings

from .serializers import GroupSerializer, ClientSerializer
from .models import Client


@api_view(['POST'])
@permission_classes([AllowAny, ])
def RegisterNumber(request):
    # get user phone number
    # generate a new number and send to user sms service
    # save number in user table in (pre-active phase)
    # return successfull status
    serializer = ClientSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def ValidateNumber(request):
    # get number from user
    # check against saved number in models
    # activate user and authenticate
    # generate new JWT token and return it

    return Response('token:123')
