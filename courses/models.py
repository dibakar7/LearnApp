from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_desc = models.TextField()
    course_img = models.ImageField(upload_to='courses_img/', max_length=255, null=True, blank= False)
    created_by = models.CharField(max_length=50)
    creator_id = models.IntegerField(null=True)
    course_notes = models.FileField(upload_to='notes/', null=True, blank=True)
    external_links = models.CharField(max_length=255, null=True, blank=True)

class Enrolled_course(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50, null=True, blank=False)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100, null=True, blank=False)
    