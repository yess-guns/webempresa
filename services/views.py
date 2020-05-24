from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def services(request):
    return render(request, "services/services.html")