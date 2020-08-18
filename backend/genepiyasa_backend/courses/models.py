from django.db import models

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
class Course(models.Model):
    course_title = models.CharField(max_length=300)
    course_detail = models.TextField(max_length=300)
    course_imglink = models.URLField(max_length = 200, null=True, blank=True)
    svg_name = models.CharField(max_length=100, null=True, blank=True)  
    def __str__(self):
        return self.course_title
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=300)
    lesson_detail = models.TextField(max_length=300)
    lesson_img = models.URLField(max_length=200, null=True, blank=True)
    svg_name = models.CharField(max_length=100, null=True, blank=True) 
    def __str__(self):
        return self.lesson_title
class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=300)
    topic_detail = models.TextField(max_length=300)
    topic_status = models.BooleanField()
    def __str__(self):
        return self.topic_title
class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic_title = models.CharField(max_length=300)
    subtopic_detail = models.TextField(max_length=500)
    subtopic_image_link = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.subtopic_title
        



