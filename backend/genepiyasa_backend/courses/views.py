from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import CourseSerializer, LessonSerializer, TopicSerializer, SubtopicSerializer, UserSerializer   # add this
from .models import Course, Lesson, Topic, Subtopic
from django.contrib.auth.models import User   
# Create your views here.
class CourseView(viewsets.ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()
class LessonView(viewsets.ModelViewSet):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
class TopicView(viewsets.ModelViewSet):
	serializer_class = TopicSerializer
	queryset = Topic.objects.all()
class SubtopicView(viewsets.ModelViewSet):
	serializer_class = SubtopicSerializer
	queryset = Subtopic.objects.all()
class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
