from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Courses, Enrolled_course
from authentication.models import Student

# Register your models here.
class courseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'created_by', 'creator_id')
    search_fields = ('course_name', 'created_by', 'creator_id')
    readonly_fields = ('course_name', 'created_by', 'creator_id')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
# class StudentInline(admin.TabularInline):
#     model = Student
class enrolled_courseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'student_id', 'student_name')
    ordering = ['course_id']

    filter_horizontal = ()
    list_filter = ()
    # list_display = ('course_name', 'display_students')
    # inlines = [StudentInline]

    # def display_students(self, obj):
    #     return ", ".join([student.name for student in obj.students.all()])

    # display_students.short_description = 'Students Enrolled'

admin.site.register(Courses, courseAdmin)
admin.site.register(Enrolled_course, enrolled_courseAdmin)