
from rest_framework import serializers
from .models import Course


# this is the basic serialzer and you should remove 'url' from fields
# class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):
	
	#
	class Meta:
		# define which model we are serializing
		model = Course 
		# fields contains id and all fields from our model (course)
		# id commes from ? is a number which is not
		# each items has un id number automatically given
		fields = ('id','url', 'name', 'language','price')