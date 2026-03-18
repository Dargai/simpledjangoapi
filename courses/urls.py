
from django.urls import path, include

#
from . import views
from rest_framework import routers

#
routers = routers.DefaultRouter()
#register it - so localhost:8000/courses point to the view.CourseView
routers.register('courses', views.CourseView) #that when we 

#it means that add the urls of the routers into the root url which is localhost:8000
# literally it let us add active localhost:8000/courses 
urlpatterns = [
    path('', include(routers.urls))
]
