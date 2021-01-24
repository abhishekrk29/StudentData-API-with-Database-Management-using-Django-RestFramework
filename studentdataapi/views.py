from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class StudentDataSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('firstname')
    serializer_class = StudentSerializer