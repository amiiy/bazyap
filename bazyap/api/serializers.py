from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Client


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('last_name', 'username', 'token', 'otp_code', 'sex', 'type')

    def create(self, validated_data):
        return Client.objects.create(**validated_data)
