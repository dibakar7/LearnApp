from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse, Http404
from authentication.models import User_Details
from courses.models import Courses, Enrolled_course
from django.http import HttpResponse
from django.core.files.images import ImageFile
from django.views.decorators.cache import cache_control
from authentication.decorators import custom_login_required

def LearnAppDefault(request):
    return render(request, "default.html")

# For student home section:
@cache_control(no_cache=True, must_revalidate=True, no_store=True, no_session=True)
@custom_login_required
def Student_Home(request):
    context = {} 
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = User_Details.objects.filter(id=user_id).first()
        if user is not None:
            context = {
                'first_name': user.first_name,
                'email': user.email,
                'id': user_id,
                'data': Courses.objects.all(),
                # add more fields as needed
            }
        else:
            print("User not found.")
    return render(request, 'student_index.html', context)

# For teacher home section:
@custom_login_required
def Teacher_Home(request, name):
    context = {} 
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = User_Details.objects.filter(id=user_id).first()
        if user is not None:
            context = {
                'teacher_item': User_Details.objects.get(id=user_id),
                'email': user.email,
                'your_courses': Courses.objects.filter(creator_id=user_id),
                'count': Courses.objects.filter(creator_id=user_id).count(),
            }
            if request.method == 'POST':
                cname = request.POST.get('courseName')
                cdesc = request.POST.get('courseDesc')
                cimg = request.FILES['courseImg']
                cnotes = request.FILES['courseNotes']
                exlinks = request.POST.get('externalLinks')
                cby = user.first_name
                creator_id = user_id

                existingInctance = Courses.objects.filter(course_name=cname).first()
                if existingInctance:
                    return HttpResponse('Course with this name already exists!')
                else:
                    instance = Courses(course_name = cname, course_desc = cdesc, course_img = ImageFile(cimg), created_by = cby, creator_id = creator_id, course_notes = cnotes, external_links = exlinks)
                    instance.save()
                return redirect('teacher-profile', name)  # Refresh the page
        else:
            print("User not found.")
    return render(request, 'teacher_profile.html', context)
@custom_login_required
def CourseViewAsTeacher(request, name, cid):
    user_id = request.session['user_id']
    context = {
        'teacher_item': User_Details.objects.get(id=user_id),
        'course_item': Courses.objects.get(id=cid),
        'noOfStudentsEnrolled': Enrolled_course.objects.filter(course_id = cid).count(),
        'nameOfEnrolledStudents': Enrolled_course.objects.filter(course_id = cid),
    }
    if request.method == 'POST':
        cdesc = request.POST.get('courseDesc')
        cnotes = request.FILES['courseNotes']
        exlinks = request.POST.get('externalLinks')
        obj = Courses.objects.get(id=cid)
        if cdesc:
            obj.course_desc = cdesc
        if cnotes:
            obj.course_notes = cnotes
        if exlinks:
            obj.external_links = exlinks
        obj.save()
    return render(request, 'courseviewasTeacher.html', context)
    

def signout(request):
    request.session.flush()
    return redirect('home')

