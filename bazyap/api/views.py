from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Client
from .serializers import ClientSerializer
from .utils import get_code


@api_view(['POST'])
@permission_classes([AllowAny, ])
def RegisterNumber(request):
    request.data['otp_code'] = get_code()
    serializer = ClientSerializer(
        data={'username': request.data['phone_number'], 'first_name': request.data['first_name'],
              'last_name': request.data['last_name'], 'otp_code': request.data['otp_code']})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def ValidateNumber(request):
    return Response('token:123')


@api_view(['POST'])
@permission_classes([AllowAny, ])
def Profile(request):
    print(request.data)
    querystring = get_object_or_404(Client, username=request.data['username'])
    data = ClientSerializer(querystring)
    return Response(data.data, status=status.HTTP_200_OK)
