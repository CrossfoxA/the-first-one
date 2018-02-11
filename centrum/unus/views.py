from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, ('unus/index.html'))

def about(request):
    return render(request, ('unus/about.html'))