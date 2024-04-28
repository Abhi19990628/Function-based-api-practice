from rest_framework import serializers
from .models import Rishab


class RishabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rishab
        fields = '__all__'