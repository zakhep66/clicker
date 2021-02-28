from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics

from app.models import Owner
from app.serializer import OwnerSerializer


def index(request):
    return render(request, 'index.html')


class OwnerView(ModelViewSet):

    queryset = Owner.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = OwnerSerializer

class OwnerDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()