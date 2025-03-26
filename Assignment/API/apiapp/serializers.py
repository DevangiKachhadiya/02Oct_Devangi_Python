from rest_framework import serializers
from .models import *

class studSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudInfo
        fields = "__all__"
        

