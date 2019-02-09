from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings

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
    # deleting otp code from model will handled by job workers
    queryset = get_object_or_404(Client, username=request.data['username'])
    print(request.data)
    profile = ClientSerializer(queryset)
    print(profile.data)
    if profile.data['otp_code'] == request.data['otp_code']:
        token = generate_token(user=profile.data)
        return Response(token, status=status.HTTP_200_OK)
    return Response('wrong password', status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def Profile(request):
    queryset = get_object_or_404(Client, username=request.data['username'])
    profile = ClientSerializer(queryset)
    return Response(profile.data, status=status.HTTP_200_OK)


def generate_token(user):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    print(user)
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def jwt_payload_handler(user):
    return {"ok": True, "user": user}
