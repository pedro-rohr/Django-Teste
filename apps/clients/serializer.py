from .models import Client, ClientSocialNetwork
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialNetwork
        fields = '__all__'
