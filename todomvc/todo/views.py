from django.shortcuts import render
from todo.models import ToDo
from rest_framework import generics
from todo.serializers import ToDoSerializer


# Create your views here.

class ToDoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
