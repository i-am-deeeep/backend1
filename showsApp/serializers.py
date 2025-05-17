from rest_framework.serializers import ModelSerializer
from showsApp.models import Show, Platform

class ShowSerializer(ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

class PlatformSerializer(ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'