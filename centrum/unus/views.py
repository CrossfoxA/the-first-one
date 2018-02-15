from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from unus.serializers import unusSerializer


# Create your views here.

def home(request):
    return render(request, ('unus/index.html'))

def about(request):
    return render(request, ('unus/about.html'))

class RestApiView(APIView):
    def get(self, request):
        serializer = unusSerializer
        return Response(serializer.data)