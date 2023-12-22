"""
URL configuration for LearnApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LearnApp import views
from authentication.views import signin, registration
from courses.views import Enroll, Course_details, My_course_work, open_pdf
from myprofile.views import Student_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LearnAppDefault, name='home'),
    path('student-home/', views.Student_Home,name='student-home'),
    path('teacher-home/<str:name>/', views.Teacher_Home, name='teacher-profile'),
    path('signin/', signin, name='signin'),
    path('register/', registration, name='register'),
    path('signout/', views.signout, name='signout'),
    path('enroll/<int:cid>/', Enroll, name='enroll'),
    path('course_details/<int:cid>/', Course_details, name='course_details'),
    path('<str:name>/my-course-work/<int:cid>', My_course_work, name='my_course_work'),
    path('<str:name>/open_pdf/<int:cid>', open_pdf, name='open_pdf'),
    path('student_profile/<str:name>/', Student_profile, name='student-profile'),
    path('Course-View/<str:name>/<int:cid>/', views.CourseViewAsTeacher, name='CourseViewAsTeacher')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)