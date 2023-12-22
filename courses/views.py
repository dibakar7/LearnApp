from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse, Http404
from django.contrib import messages
from authentication.models import User_Details
from courses.models import Courses, Enrolled_course
from authentication.decorators import custom_login_required
# Create your views here.

@custom_login_required
def Enroll(request, cid):
    user_id = request.session['user_id']
    user = User_Details.objects.get(id=user_id)
    print("enroll fn was checked")
    try:
        current_course = Courses.objects.get(id = cid)
        instance = Enrolled_course(student_id = user_id , student_name = user.first_name, course_id = cid, course_name=current_course.course_name)
        instance.save()
        
    except Courses.DoesNotExist:
        # handle the case where no course with the given id exists
        pass
    except Courses.MultipleObjectsReturned:
        # handle the case where multiple courses have the given id
        pass
    return redirect('course_details', cid=cid)

@custom_login_required
def Course_details(request, cid):
    user_id = request.session['user_id']
    print("course details fn was checked")
    print(cid)
    print(user_id)
    
    # Check if the user is enrolled in the course
    # is_enrolled = Enrolled_course.objects.filter(student_id=user_id, course_id=cid).exists()

    # Pass the flag to the template
    is_enrolled = Enrolled_course.objects.filter(student_id=user_id, course_id=cid).exists()
    print(is_enrolled)
    context = {'course_item': Courses.objects.get(id=cid), 'student_item':User_Details.objects.get(id=user_id), 'is_enrolled':is_enrolled,}
    return render(request,'course_details.html', context)

@custom_login_required
def My_course_work(request, name, cid):
    user_id = request.session['user_id']
    context = {'course_item': Courses.objects.get(id=cid), 'student_item':User_Details.objects.get(id=user_id), }
    return render(request, 'my-course-work.html', context)

@custom_login_required
def open_pdf(request, name, cid):
    course = Courses.objects.get(id=cid)
    path = course.course_notes
    try:
        return FileResponse(open(path.path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
@custom_login_required
def Create_courses(request):
    tid = request.session["user_id"]
    if request.method == 'POST':
        c_name = request.POST.get()
        c_desc = request.POST.get()
        c_img = request.POST.get()
        created_by = User_Details.objects.get(id = tid).first_name
        creator_id = tid
        c_notes = request.POST.get()
        ex_links = request.POST.get()

        instance = Courses(course_name = c_name, course_desc = c_desc, course_img = c_img, created_by = created_by, creator_id = creator_id, course_notes = c_notes, external_links = ex_links)
        instance.save()
        messages.success(request, 'Course created successfully!')
    return render(request, 'create-course.html')
    