from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Owner
from app.serializer import OwnerSerializer


@api_view(['GET', 'POST'])
def owner_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        owner = Owner.objects.all()
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)