from rest_framework import serializers
from .models import Abhishek

class AbhishekSerializers(serializers.ModelSerializer):
    class Meta:
        model = Abhishek,
        fields = '__all__'
