from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_Details, Student, Teacher
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
# Register your models here.

class User_DetailsAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_student', 'is_teacher', 'is_admin', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'date_joined')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_student', 'is_teacher', 'groups', 'user_permissions')}),
    )

class StudentAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'date_joined')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TeacherAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'date_joined')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User_Details, User_DetailsAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
