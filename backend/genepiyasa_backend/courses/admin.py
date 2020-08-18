from django.contrib import admin
from .models import Course, Lesson, Topic, Subtopic

class TopicAdmin(admin.ModelAdmin):
    fields = ['topic_title', 'topic_link', 'lesson', 'topic_status']

class LessonAdmin(admin.ModelAdmin):
	fields = ['lesson_title', 'course']
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Topic)
admin.site.register(Subtopic)


