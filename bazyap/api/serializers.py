from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Client
from .utils import get_code


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'username', 'token', 'otp_code')

    def create(self, validated_data):
        # return Client.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'],
        #                              username=validated_data['phone_number'])
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
