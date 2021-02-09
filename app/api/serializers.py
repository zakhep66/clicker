from rest_framework import serializers
from ..models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'nick', 'total_data')