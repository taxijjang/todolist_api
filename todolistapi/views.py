from django.shortcuts import render
from rest_framework import viewsets

from .serializer import  DoListSerializer, DoneListSerializer
from .models import DoList, DoneList

class DoListViewSet(viewsets.ModelViewSet):
    queryset = DoList.objects.all()
    serializer_class = DoListSerializer

class DoneListViewSet(viewsets.ModelViewSet):
    queryset = DoneList.objects.all()
    serializer_class = DoneListSerializer