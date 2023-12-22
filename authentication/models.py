from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Create your models here., related_name='user_details_groups'
class UserDetailsManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")
        if not first_name:
            raise ValueError("User must have first name.")
        if not last_name:
            raise ValueError("User must have last name.")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User_Details(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email Address", unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # Password Field
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    type = models.CharField(max_length=1)
    
    groups = models.ManyToManyField(Group, related_name='user_details_set')
    user_permissions = models.ManyToManyField(Permission, related_name='user_details_set')
    
    objects = UserDetailsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
# Code for proxy models:
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_student=True)

class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_teacher=True)

class Student(User_Details):
    objects = StudentManager()

    class Meta:
        proxy = True

class Teacher(User_Details):
    objects = TeacherManager()

    class Meta:
        proxy = True