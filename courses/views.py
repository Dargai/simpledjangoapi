from django.shortcuts import render
#
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseView(viewsets.ModelViewSet):
	# which model / database we will use
	queryset = Course.objects.all()  #get all courses from dbb
	# which serializers we should use
	serializer_class = CourseSerializer
