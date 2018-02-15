from rest_framework import serializers
from unus.models import unusListElements

class unusSerializer(serializers.ModelSerializer):
    class Meta:
        model = unusListElements
        fields = 'id', 