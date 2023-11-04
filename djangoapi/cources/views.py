from django.shortcuts import render
from rest_framework import viewsets
from .models import Cource
from .serializer import CourceSerializer

class CourceView(viewsets.ModelViewSet):
    queryset = Cource.objects.all()
    serializer_class = CourceSerializer

# Create your views here.