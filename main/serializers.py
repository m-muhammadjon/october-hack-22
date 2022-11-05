from rest_framework import serializers

from main import models


class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advocate
        fields = '__all__'
