from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse, Http404
from authentication.models import User_Details
from courses.models import Courses, Enrolled_course

# Create your views here.
def Student_profile(request, name):
    sid = request.session['user_id']
    context = {'student_item': User_Details.objects.get(id=sid), 'course_item': Enrolled_course.objects.filter(student_id=sid),}
    return render(request, 'student-profile.html', context)