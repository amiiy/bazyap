from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import Client
from .serializers import ClientSerializer
from .utils import get_code


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def test(request):
    return Response('ok')


@api_view(['POST'])
@permission_classes([AllowAny, ])
def RegisterNumber(request):
    request.data['otp_code'] = get_code()
    serializer = ClientSerializer(
        data={'username': request.data['phone_number'],
              'last_name': request.data['last_name'], 'sex': request.data['sex'], 'otp_code': request.data['otp_code']
              })
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def ValidateNumber(request):
    # deleting otp code from model will handled by job workers
    queryset = get_object_or_404(Client, username=request.data['phone_number'])
    profile = ClientSerializer(queryset)
    if profile.data['otp_code'] == request.data['otp_code']:
        queryset.is_valid_phone_number = True
        queryset.save()
        return Response(status=status.HTTP_200_OK)
    return Response('wrong password', status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    otp_code = get_code()
    user = get_object_or_404(Client, username=request.data['phone_number'])
    user.otp_code = otp_code
    # send otp_code => SMS
    return Response('SMS Send to your phone', status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_token(request):
    user = get_object_or_404(Client, username=request.data['phone_number'])
    if user.otp_code == request.data['otp_code']:
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token, 'user': user}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def Profile(request):
    queryset = get_object_or_404(Client, username=request.data['username'])
    profile = ClientSerializer(queryset)
    return Response(profile.data, status=status.HTTP_200_OK)
