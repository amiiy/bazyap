from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Client


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ClientSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    otp_code = 1234
    token = "secret_token"

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.name)
        return instance

    def validate(self, attrs):
        """
        check attrs for validations
        return validated data
        """
        if 0:
            raise serializers.ValidationError("some crazy excepction here!")
        return attrs
