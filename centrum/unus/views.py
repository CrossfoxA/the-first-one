from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from unus.serializers import unusSerializer

from unus.models import unusListElements


# Create your views here.

def home(request):
    return render(request, ('unus/index.html'))

def about(request):
    return render(request, ('unus/about.html'))

class RestApiListView(APIView):
    def get(self, request):
        items = unusListElements.objects.all()
        serializer = unusSerializer(items, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = unusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestApiDetailedView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(unusListElements, pk=pk)
        serializer = unusSerializer(item)
        return Response(serializer.data)

    def delete(self, request, pk):
        item = get_object_or_404(unusListElements, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
