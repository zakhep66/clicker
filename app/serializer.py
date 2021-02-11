from rest_framework.serializers import ModelSerializer
from app.models import Owner


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'