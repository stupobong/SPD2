from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
#sending emails
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core import mail
from django.core.mail.message import EmailMessage
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.template.loader import render_to_string
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import User, Group
from .filters import *
from django.http import JsonResponse
from tablib import Dataset
from django.db.models import Q
from .resources import Entrance_ExamResources

from .forms import *
from .models import *
from .admin import *



#Views
@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get ('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('admin_menu')
        else:
            messages.error(request, 'Invalid username or Password')
    context = {}
    return render(request, 'accounts/loginpage.html', context)

#---------------------------------------------------------------Login Functions Admin/Registrar/Student-------------------------------------------------------------------
#Login Admin
@login_required(login_url='login')
@admin_only
def admin_menu(request):
    return render(request, 'homepages/admin/admin_menu.html')

#Login Registrar
@login_required(login_url='login')
def registrar_menu(request):
    return render(request, 'homepages/registrar/registrar_menu.html')
#---------------------------------------------------------------------------- Change Password ---------------------------------------------------------------------------
#Update Password Registrar
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def change_password2(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password successfully updated')
            return render(request, 'homepages/registrar/registrar_menu.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'homepages/registrar/account_management/change_password.html', {
        'form': form
    })

#Change Password Student
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def change_student_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password successfully updated')
            return render(request, 'homepages/student/student_menu.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'homepages/student/account_management/update_password.html', {
        'form': form
    })
#Update Password Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password successfully updated')
            return render(request, 'homepages/admin/admin_menu.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'homepages/admin/user_management/admin-user/change_password.html', {
        'form': form
    })

     
#Login Student
@login_required(login_url='login')
def student_menu(request):
    return render(request, 'homepages/student/student_menu.html')

#Login Guest
@login_required(login_url='login')
def guest_user_menu(request):
    return render(request, 'homepages/user/guest_user_menu.html')

#-----------------------------------------------------------User Management Admin/Registrar/Student---------------------------------------------------------------

#Create Admin User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_admin_user(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/admin/user_management/admin-user/create_admin_user.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.get(name="admin")
        user.groups.add(group)
        admin = User.objects.all().filter(groups__name="admin")
        messages.success(request, 'Admin User Sucessfully Registered')
        admin = User.objects.all().filter(groups__name="admin")
        return render(request, 'homepages/admin/user_management/admin-user/view_admin.html', {'admin': admin})
    else:    
        args['form'] = form
        return render(request, 'homepages/admin/user_management/admin-user/create_admin_user.html', args)

#-----------------------------------------------------------View User Management-Admin ----------------------------------------------------------------------------------------------

#-------------- Filter Search User Management ----------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','registrar','student','staff'])
def user_management(request):
    users = User.objects.all().order_by('-date_joined')
    if 'q' in request.GET:
        q =request.GET['q']
        users = User.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(username__icontains=q)|Q(groups__name__icontains=q))
    users_count = users.count()
    
    context = {
        'users':users,
        'users_count': users_count
    }
    return render(request, 'homepages/admin/user_management/users/view_users.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_user_management(request):
    users = User.objects.all()
    if 'q' in request.GET:
        q =request.GET['q']
        users = User.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(username__icontains=q))
    users_count = users.count()
    
    context = {
        'users':users,
        'users_count': users_count
    }
    return render(request, 'homepages/admin/user_management/users/view_users.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def prospect_management(request):
    prospect = Prospect.objects.all()
    if 'q' in request.GET:
        q =request.GET['q']
        prospect = Prospect.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(apply_grade_level__icontains=q))
    prospect_count = prospect.count()
    
    context = {
        'prospect':prospect,
        'prospect_count': prospect_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/registree/view_prospect.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def entr_management(request):
    entr_xview = Entrance_Exam.objects.all().order_by('-date_exam')
    if 'q' in request.GET:
        q =request.GET['q']
        entr_xview = Entrance_Exam.objects.filter(Q(class_name__icontains=q)|Q(time_schedule__icontains=q))
    entr_xview_count = entr_xview.count()
    
    context = {
        'entr_xview':entr_xview,
        'entr_xview_count': entr_xview_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entr_xview.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def xview_management(request):
    enroll_xview = Enroll_Exam.objects.all().order_by('-date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        enroll_xview = Enroll_Exam.objects.filter(Q(prospect_name__first_name__icontains=q)|Q(username__icontains=q)|Q(prospect_name__last_name__icontains=q))
    prospect_count = enroll_xview.count()
    
    context = {
        'enroll_xview':enroll_xview,
        'prospect_count': prospect_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xview.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def xstats_management(request):
    exam_stats = Exam_Stats.objects.all().order_by('date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        exam_stats = Exam_Stats.objects.filter(Q(exam_card__prospect_name__first_name__icontains=q)|Q(exam_card__prospect_name__last_name__icontains=q)|Q(exam_card__username__icontains=q)|Q(exam_type__icontains=q))
    prospect_count = exam_stats.count()
    
    
    context = {
        'exam_stats':exam_stats,
        'prospect_count': prospect_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xview.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def subject_management(request):
    subj_view = Subject.objects.all().order_by('grade_level')
    if 'q' in request.GET:
        q =request.GET['q']
        subj_view = Subject.objects.filter(Q(grade_level__icontains=q))
    grade_level_count = subj_view.count()
    
    context = {
        'subj_view':subj_view,
        'grade_level_count': grade_level_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def classr_management(request):
    classr_view = Classroom.objects.all().order_by('date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        classr_view = Classroom.objects.filter(Q(class_level__icontains=q)|Q(class_bld__icontains=q))
    classr_count = classr_view.count()
    
    context = {
        'classr_view':classr_view,
        'classr_count': classr_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def asgclass_management(request):
    asgclass_view = Assign_Class.objects.all().order_by('grade_level')
    if 'q' in request.GET:
        q =request.GET['q']
        asgclass_view = Assign_Class.objects.filter(Q(class_level__class_level__icontains=q)|Q(homeroom_teacher__first_name__icontains=q))
    asgclass_count = asgclass_view.count()
    
    context = {
        'asgclass_view':asgclass_view,
        'asgclass_count':asgclass_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def xstudent_management(request):
    student = Student.objects.all().order_by('-date_joined')
    if 'q' in request.GET:
        q =request.GET['q']
        student = Student.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(user__icontains=q))
    student_count = student.count()
    
    
    context = {
        'student':student,
        'student_count': student_count
    }
    return render(request, 'homepages/student/re-enroll/xstudent_view.html', context)

#--------------- Update User -----------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_user(request, user_id=0):
    args = {}
    if request.method == "GET":
        if user_id==0:
            form    = updateuserform()
        else: 
            users  = User.objects.get(pk=user_id)
            form    = updateuserform(instance=users)
        return render(request, 'homepages/admin/user_management/users/update_user.html', {'form': form})
    else:
        if user_id==0:
            form    = userform(request.POST)
        else:
            users  =  User.objects.get(pk=user_id)
            form    =  updateuserform(request.POST, instance=users)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Sucessfully Updated')
            users = User.objects.all()
            return render(request, 'homepages/admin/user_management/users/view_users.html', {'users': users})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/users/update_user.html', args)

#Update Prospect
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_prospect(request, pros_id=0):
    args = {}
    if request.method == "GET":
        if pros_id==0:
            form    = updateprospectform()
        else: 
            prospect  = Prospect.objects.get(pk=pros_id)
            form    = updateprospectform(instance=prospect)
        return render(request, 'homepages/registrar/manage_enrollment/registree/update_prospect.html', {'form': form})
    else:
        if pros_id==0:
            form    = updateprospectform(request.POST)
        else:
            prospect  =  Prospect.objects.get(pk=pros_id)
            form    =  updateprospectform(request.POST, request.FILES, instance=prospect)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prospect Sucessfully Updated')
            prospect = Prospect.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/registree/view_prospect.html', {'prospect': prospect})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/registree/update_prospect.html', {'form': form})

#Update Entrance Exam
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_entrancex(request, entr_exam_id=0):
    args = {}
    if request.method == "GET":
        if entr_exam_id==0:
            form    = updateentrance_examform()
        else: 
            entr_xview  = Entrance_Exam.objects.get(pk=entr_exam_id)
            form    = updateentrance_examform(instance=entr_xview)
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_entrancex.html', {'form': form})
    else:
        if entr_exam_id==0:
            form    = updateentrance_examform(request.POST)
        else:
            entr_xview  =  Entrance_Exam.objects.get(pk=entr_exam_id)
            form    =  updateentrance_examform(request.POST, request.FILES, instance=entr_xview)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrance Exam Sucessfully Updated')
            entr_xview = Entrance_Exam.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entr_xview.html', {'entr_xview': entr_xview})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_entrancex.html', {'form': form})

#Update Entrance Exam Status
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_statsx(request, exam_stats_id=0):
    args = {}
    if request.method == "GET":
        if exam_stats_id==0:
            form    = updateexam_statsform()
        else: 
            exam_stats  = Exam_Stats.objects.get(pk=exam_stats_id)
            form    = updateexam_statsform(instance=exam_stats)
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_statsx.html', {'form': form})
    else:
        if exam_stats_id==0:
            form    = updateexam_statsform(request.POST)
        else:
            exam_stats  =  Exam_Stats.objects.get(pk=exam_stats_id)
            form    =  updateexam_statsform(request.POST, request.FILES, instance=exam_stats)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrance Exam Sucessfully Updated')
            exam_stats = Exam_Stats.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xview.html', {'exam_stats': exam_stats})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_statsx.html', {'form': form})

#Update Entrance Exam Attributes enroll_xview
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_xenroll(request, enroll_xview_id=0):
    args = {}
    if request.method == "GET":
        if enroll_xview_id==0:
            form    = updateenroll_examform()
        else: 
            enroll_xview  = Enroll_Exam.objects.get(pk=enroll_xview_id)
            form    = updateenroll_examform(instance=enroll_xview)
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_xenroll.html', {'form': form})
    else:
        if enroll_xview_id==0:
            form    = updateenroll_examform(request.POST)
        else:
            enroll_xview  =  Enroll_Exam.objects.get(pk=enroll_xview_id)
            form    =  updateenroll_examform(request.POST, request.FILES, instance=enroll_xview)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enroll Entrance Exam Sucessfully Updated')
            enroll_xview = Enroll_Exam.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xview.html', {'enroll_xview': enroll_xview})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/update_xenroll.html', {'form': form})

#Update Subject
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_subject(request, class_sbj_id=0):
    args = {}
    if request.method == "GET":
        if class_sbj_id==0:
            form    = updatesubjectform()
        else: 
            subj_view  = Subject.objects.get(pk=class_sbj_id)
            form    = updatesubjectform(instance=subj_view)
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_subject.html', {'form': form})
    else:
        if class_sbj_id==0:
            form    = updatesubjectform(request.POST)
        else:
            subj_view  =  Subject.objects.get(pk=class_sbj_id)
            form    =  updatesubjectform(request.POST, request.FILES, instance=subj_view)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Sucessfully Updated')
            subj_view = Subject.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_view.html', {'subj_view': subj_view})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_subject.html', {'form': form})

#Update Classroom Enrollment
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_classr(request, classr_view_id=0):
    args = {}
    if request.method == "GET":
        if classr_view_id==0:
            form    = updateclassroomform()
        else: 
            classr_view  = Classroom.objects.get(pk=classr_view_id)
            form    = updateclassroomform(instance=classr_view)
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_classr.html', {'form': form})
    else:
        if classr_view_id==0:
            form    = updateclassroomform(request.POST)
        else:
            classr_view  =  Classroom.objects.get(pk=classr_view_id)
            form    =  updateclassroomform(request.POST, request.FILES, instance=classr_view)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom Sucessfully Updated')
            classr_view = Classroom.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_view.html', {'classr_view': classr_view})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_classr.html', {'form': form})

#Update Assigned Class
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_assigned_class(request, assigned_class_id=0):
    args = {}
    if request.method == "GET":
        if assigned_class_id==0:
            form    = updateassign_classform()
        else: 
            assigned_class  = Assign_Class.objects.get(pk=assigned_class_id)
            form    = updateassign_classform(instance=assigned_class)
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_assigned_class.html', {'form': form})
    else:
        if assigned_class_id==0:
            form    = updateassign_classform(request.POST)
        else:
            assigned_class  =  Assign_Class.objects.get(pk=assigned_class_id)
            form    =  updateassign_classform(request.POST, request.FILES, instance=assigned_class)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assigned Class Sucessfully Updated')
            assigned_class = Assign_Class.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class.html', {'assigned_class': assigned_class})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/update_assigned_class.html', {'form': form})

#Update Staff 
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_staff(request, staff_id=0):
    args = {}
    if request.method == "GET":
        if staff_id==0:
            form    = updatestaffform()
        else: 
            staff  = Staff.objects.get(pk=staff_id)
            form    = updatestaffform(instance=staff)
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/update_staff.html', {'form': form})
    else:
        if staff_id==0:
            form    = updatestaffform(request.POST)
        else:
            staff  =  Staff.objects.get(pk=staff_id)
            form    =  updatestaffform(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff Sucessfully Updated')
            staff = Staff.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staffs_view.html', {'staff': staff})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/update_staff.html', {'form': form})

#Update Staff 
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_staff_user(request, staff_user_id=0):
    args = {}
    if request.method == "GET":
        if staff_user_id==0:
            form    = updatestaff_userform()
        else: 
            staff_user  = Staff_User.objects.get(pk=staff_user_id)
            form    = updatestaff_userform(instance=staff_user)
        return render(request, 'homepages/admin/user_management/users/update_staff_user.html', {'form': form})
    else:
        if staff_user_id==0:
            form    = updatestaff_userform(request.POST)
        else:
            staff_user  =  Staff_User.objects.get(pk=staff_user_id)
            form    =  updatestaff_userform(request.POST, request.FILES, instance=staff_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff Sucessfully Updated')
            staff_user = Staff_User.objects.all()
            return render(request, 'homepages/admin/user_management/users/staff_users_view.html', {'staff_user': staff_user})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/users/update_staff_user.html', {'form': form})

#Update Teacher
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_teacher(request, teacher_id=0):
    args = {}
    if request.method == "GET":
        if teacher_id==0:
            form    = updateteacherform()
        else: 
            teacher  = Teacher.objects.get(pk=teacher_id)
            form    = updateteacherform(instance=teacher)
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/update_teacher.html', {'form': form})
    else:
        if teacher_id==0:
            form    = updateteacherform(request.POST)
        else:
            teacher  =  Teacher.objects.get(pk=teacher_id)
            form    =  updateteacherform(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Sucessfully Updated')
            teacher = Teacher.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_view.html', {'teacher': teacher})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/update_teacher.html', {'form': form})
        
#--------------Update Users Password ----------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_user_password(request, password_id=0):
    args = {}
    if request.method == "GET":
        if password_id==0:
            form    = updatepassword()
        else: 
            users  = User.objects.get(pk=password_id)
            form    = updatepassword(instance=users)
        return render(request, 'homepages/admin/user_management/users/update_user_password.html', {'form': form})
    else:
        if password_id==0:
            form    = updatepassword(request.POST)
        else:
            users  =  User.objects.get(pk=password_id)
            form    =  updatepassword(request.POST, instance=users)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Sucessfully Updated')
            users = User.objects.all()
            return render(request, 'homepages/admin/user_management/users/view_user.html', {'users': users})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/users/update_user_password.html', args)


#Create Registrar User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def create_registrar_user(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/admin/user_management/registrar-user/create_registrar_user.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.get(name="registrar")
        user.groups.add(group)
        registrar = User.objects.all().filter(groups__name="registrar")
        messages.success(request, 'Registrar User Sucessfully Registered')
        registrar = User.objects.all().filter(groups__name="registrar")
        return render(request, 'homepages/admin/user_management/registrar-user/view_registrar_user.html', {'registrar': registrar})
    else:    
        args['form'] = form
        return render(request, 'homepages/admin/user_management/registrar-user/create_registrar_user.html', args)

#Create Staff User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def create_staff_user(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/admin/user_management/staff_user/create_staff_user.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.get(name="staff")
        user.groups.add(group)
        staff_user = User.objects.all().filter(groups__name="staff")
        messages.success(request, 'Staff User Sucessfully Registered')
        staff_user = User.objects.all().filter(groups__name="staff")
        return render(request, 'homepages/admin/user_management/users/view_users.html', {'staff_user': staff_user})
    else:    
        args['form'] = form
        return render(request, 'homepages/admin/user_management/staff_user/create_staff_user.html', args)

#Create Student User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def create_student_user(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/admin/user_management/student-user/create_student_user.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.get(name="student")
        user.groups.add(group)
        student = User.objects.all().filter(groups__name="student")
        messages.success(request, 'Student Sucessfully Registered')
        student = User.objects.all().filter(groups__name="student")
        return render(request, 'homepages/admin/user_management/student-user/view_student.html', {'student': student})
    else:    
        args['form'] = form
        return render(request, 'homepages/admin/user_management/student-user/create_student_user.html', args)

#Create Guest User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_guest_user(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/admin/user_management/guest-user/create_guest_user.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.get(name="guest")
        user.groups.add(group)
        guest = User.objects.all().filter(groups__name="guest")
        messages.success(request, 'Guest Sucessfully Registered')
        guest = User.objects.all().filter(groups__name="guest")
        return render(request, 'homepages/admin/user_management/guest-user/view_guest_user.html', {'guest': guest})
    else:    
        args['form'] = form
        return render(request, 'homepages/admin/user_management/guest-user/create_guest_user.html', args)

#Create Staff User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','registrar'])
def staff_form(request):
    args = {}
    if request.method == "GET":
        form    = userform()
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_form.html', {'form': form})
    else:
        form    = userform(request.POST)
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.all()
        user.groups.add(group)
        student = User.objects.all().filter(groups__name="student")
        messages.success(request, 'Student Sucessfully Registered')
        student = User.objects.all().filter(groups__name="student")
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'student': student})
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.all()
        user.groups.add(group)
        teacher = User.objects.all().filter(groups__name="teacher")
        messages.success(request, 'Teacher Sucessfully Registered')
        teacher = User.objects.all().filter(groups__name="teacher")
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'teacher': teacher})
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.all()
        user.groups.add(group)
        registrar = User.objects.all().filter(groups__name="registrar")
        messages.success(request, 'Registrar Sucessfully Registered')
        registrar = User.objects.all().filter(groups__name="registrar")
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'registrar': registrar})
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.all()
        user.groups.add(group)
        staff = User.objects.all().filter(groups__name="staff")
        messages.success(request, 'Staff Sucessfully Registered')
        staff = User.objects.all().filter(groups__name="staff")
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'staff': staff})
    if form.is_valid():
        user    = form.save()
        group   = Group.objects.all()
        user.groups.add(group)
        admin = User.objects.all().filter(groups__name="admin")
        messages.success(request, 'Registrar Sucessfully Registered')
        admin = User.objects.all().filter(groups__name="admin")
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'admin': admin})
    else:    
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_form.html', args)

#-----------------------------------------------------------Update User Management Admin/Registrar/Student---------------------------------------------------------------
    
#Update Admin User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_admin_user(request, admin_id=0):
    args = {}
    if request.method == "GET":
        if admin_id==0:
            form    = updateuserform()
        else: 
            user  = User.objects.get(pk=admin_id)
            form    = updateuserform(instance=user)
        return render(request, 'homepages/admin/user_management/admin-user/update_admin_user.html', {'form': form})
    else:
        if admin_id==0:
            form    = userform(request.POST)
        else:
            user  =  User.objects.get(pk=admin_id)
            form    =  updateuserform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin User Sucessfully Updated')
            admin = User.objects.all().filter(groups__name="admin")
            return render(request, 'homepages/admin/user_management/admin-user/update_admin_user.html', {'admin': admin})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/admin-user/view_admin.html', args)

#Update Admin Password
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def change_password1(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password successfully updated')
            return render(request, 'homepages/admin/admin_menu.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'homepages/admin/user_management/admin-user/change_password1.html', {
        'form': form
    })

#Update Guest User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_guest_user(request, guest_id=0):
    args = {}
    if request.method == "GET":
        if guest_id==0:
            form    = updateuserform()
        else: 
            user  = User.objects.get(pk=guest_id)
            form    = updateuserform(instance=user)
        return render(request, 'homepages/admin/user_management/guest-user/update_guest_user.html', {'form': form})
    else:
        if guest_id==0:
            form    = userform(request.POST)
        else:
            user  =  User.objects.get(pk=guest_id)
            form    =  updateuserform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guest User Sucessfully Updated')
            guest = User.objects.all().filter(groups__name="guest")
            return render(request, 'homepages/admin/user_management/guest-user/update_guest_user.html', {'guest': guest})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/guest-user/view_guest.html', args)

#Update Guest Password
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_guest_password(request, password_id=0):
    args = {}
    if request.method == "GET":
        if password_id==0:
            form    = updatepassword()
        else: 
            user  = User.objects.get(pk=password_id)
            form    = updatepassword(instance=user)
        return render(request, 'homepages/admin/user_management/guest-user/update_guest_password.html', {'form': form})
    else:
        if password_id==0:
            form    = updatepassword(request.POST)
        else:
            user  =  User.objects.get(pk=password_id)
            form    =  updatepassword(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guest Password Sucessfully Updated')
            guest = User.objects.all().filter(groups__name="guest")
            return render(request, 'homepages/admin/user_management/guest-user/view_guest.html', {'guest': guest})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/guest-user/update_guest_password.html', args)

#Update Registrar User
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def update_registrar_user(request, admin_id=0):
    args = {}
    if request.method == "GET":
        if admin_id==0:
            form    = updateuserform()
        else: 
            user  = User.objects.get(pk=admin_id)
            form    = updateuserform(instance=user)
        return render(request, 'homepages/admin/user_management/admin-user/update-user.html', {'form': form})
    else:
        if admin_id==0:
            form    = userform(request.POST)
        else:
            user  =  User.objects.get(pk=admin_id)
            form    =  updateuserform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin User Sucessfully Updated')
            admin = User.objects.all().filter(groups__name="admin")
            return render(request, 'homepages/admin/user_management/registrar-user/view_registrar_user.html', {'admin': admin})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/admin-user/update-user.html', args)

#Update Registrar Password
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_registrar_password(request, password_id=0):
    args = {}
    if request.method == "GET":
        if password_id==0:
            form    = updatepassword()
        else: 
            user  = User.objects.get(pk=password_id)
            form    = updatepassword(instance=user)
        return render(request, 'homepages/registrar/account_management/update_registrar_password.html', {'form': form})
    else:
        if password_id==0:
            form    = updatepassword(request.POST)
        else:
            user  =  User.objects.get(pk=password_id)
            form    =  updatepassword(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrar Password Sucessfully Updated')
            registrar = User.objects.all().filter(groups__name="registrar")
            return render(request, 'homepages/registrar/account_management/view_registrar_user.html', {'registrar': registrar})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/account_management/update_registrar_password.html', args)

#Update Student User
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_student_user(request, student_id=0):
    if request.method == "GET":
        if student_id==0:
            form    = updateuserform()
        else: 
            user  = User.objects.get(pk=student_id)
            form    = updateuserform(instance=user)
        return render(request, 'homepages/admin/user_management/student-user/update_student.html', {'form': form})
    else:
        if student_id==0:
            form    = userform(request.POST)
        else:
            user  =  User.objects.get(pk=student_id)
            form    =  updateuserform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Sucessfully Updated')
        student = User.objects.all().filter(groups__name="student")
        return render(request, 'homepages/admin/user_management/student-user/view_student.html', {'student': student})
    
#Update Student Password
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def update_student_password(request, password_id=0):
    args = {}
    if request.method == "GET":
        if password_id==0:
            form    = updatepassword()
        else: 
            user  = User.objects.get(pk=password_id)
            form    = updatepassword(instance=user)
        return render(request, 'homepages/admin/user_management/student-user/update_student_password.html', {'form': form})
    else:
        if password_id==0:
            form    = updatepassword(request.POST)
        else:
            user  =  User.objects.get(pk=password_id)
            form    =  updatepassword(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Password Sucessfully Updated')
            student = User.objects.all().filter(groups__name="student")
            return render(request, 'homepages/admin/user_management/student-user/view_student.html', {'student': student})
        else:
            args['form'] = form
            return render(request, 'homepages/admin/user_management/student-user/view_student.html', args)
        
#--------------------------------------------------------------------------Delete Functions-----------------------------------------------------------------------------------------
#Admin Delete Admin
def delete_student(request, admin_id=0):
    admin = User.objects.get(pk=admin_id)
    admin.delete()
    admin = User.objects.all()
    return render(request, 'homepages/admin/manage_enrollment/menu_page/view_users.html', {'admin': admin})

#Admin Delete User
def delete_user(request, user_id=0):
    users = User.objects.get(pk=user_id)
    users.delete()
    users = User.objects.all()
    return render(request, 'homepages/admin/user_management/users/view_users.html', {'users': users})
       
#Admin Delete Student
def delete_student(request, student_id=0):
    student = Student.objects.get(pk=student_id)
    student.delete()
    student = Student.objects.all()
    return render(request, 'homepages/admin/manage_enrollment/menu_page/view_student.html', {'student': student})

#Admin Delete Staff
def delete_staff(request, staff_id=0):
    staff = Staff.objects.get(pk=staff_id)
    staff.delete()
    staff = Staff.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staffs_view.html', {'staff': staff})

#Admin Delete Staff User
def delete_staff_user(request, staff_user_id=0):
    staff = Staff_User.objects.get(pk=staff_user_id)
    staff.delete()
    staff = Staff_User.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/view_staff_user.html', {'staff': staff})

#Admin Delete Registrar
def delete_registrar(request, registrar_id=0):
    registrar = User.objects.get(pk=registrar_id)
    registrar.delete()
    registrar = User.objects.all()
    return render(request, 'homepages/admin/manage_enrollment/view_registree/registree_view.html', {'registrar': registrar})

#Admin Delete Entrance Exam Attributes
def delete_entr_exam(request, entr_exam_id=0):
    entr_xview = Entrance_Exam.objects.get(pk=entr_exam_id)
    entr_xview.delete()
    entr_xview = Entrance_Exam.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entr_xview.html', {'entr_xview': entr_xview})

#Admin Delete Classroom Subject
def delete_class_sbj(request, class_sbj_id=0):
    class_sbj = Subject.objects.get(pk=class_sbj_id)
    class_sbj.delete()
    class_sbj = Subject.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_view.html', {'class_sbj': class_sbj})

#Admin Delete Assigned Classroom
def delete_classroom(request, classr_view_id=0):
    classr_view = Classroom.objects.get(pk=classr_view_id)
    classr_view.delete()
    classr_view = Classroom.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_view.html', {'classr_view': classr_view})

#Admin Delete Each Student
def delete_xstudent(request, student_id=0):
    student = Student.objects.get(pk=student_id)
    student.delete()
    student = Student.objects.all()
    return render(request, 'homepages/student/re-enroll/xstudent_view.html', {'student': student})

#Admin Delete Assigned Class
def delete_assigned_class(request, assigned_class_id=0):
    assigned_class = Assign_Class.objects.get(pk=assigned_class_id)
    assigned_class.delete()
    assigned_class = Assign_Class.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class.html', {'assigned_class': assigned_class})

#-----------------------------------------------------------ViewUser Management Admin/Registrar/Student---------------------------------------------------------------

#View_Users
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','registrar'])
def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'homepages/admin/user_management/users/view_groups.html', {'groups': groups})

#View_Users
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','registrar'])
def view_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'homepages/admin/user_management/users/view_users.html', {'users': users})

#View_Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_admin(request):
    admin = User.objects.all().filter(groups__name="admin")
    return render(request, 'homepages/admin/user_management/admin-user/view_admin.html', {'admin': admin})

#View Each Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def admin_profile(request, admin_id):
    admin = User.objects.get(pk=admin_id).filter(groups__name="admin")
    return render(request, 'homepages/admin/user_management/admin-user/admin_profile.html', {'admin': admin})

#View_Registrar
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_registrar_user(request):
    registrar = User.objects.all().filter(groups__name="registrar")
    return render(request, 'homepages/admin/user_management/registrar-user/view_registrar_user.html', {'registrar': registrar})

#Admin view student
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_student(request):
    student = User.objects.all().filter(groups__name="student")
    return render(request, 'homepages/admin/user_management/student-user/view_student.html', {'student': student})

#View Each Student
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'homepages/admin/user_management/student-user/view_each_student.html', {'student': student})

#Admin View Staff
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','registrar'])
def staff_view(request):
    staff = User.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_view.html', {'staff': staff})

#Admin view guest
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_guest(request):
    guest = User.objects.all().filter(groups__name="guest")
    return render(request, 'homepages/admin/user_management/guest-user/view_guest_user.html', {'guest': guest})

#-----------------------------------------------------------------Upload Excel Form---------------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def importExcel(request):
    args = {}
    if request.method == 'GET':
        x_resources = Entrance_ExamResources()
        dataset = Dataset()
        new_registree = request.FILES['my_file']
        imported_data = dataset.load(new_registree.read(), format='xlsx')
        for data in imported_data:
            value = Entrance_Exam(
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
    return render(request, 'accounts/import.html', {'x_resources': x_resources})
    

#-----------------------------------------------------------------Add Application Form---------------------------------------------------------
 
#add Registration Form
#login_required(login_url='login')
#allowed_users(allowed_roles=['registrar', 'admin','student'])
def application_form(request):
    args = {}
    if request.method == "GET":
        form    = Registreeform()
        return render(request, 'homepages/user/menu-page/application_form.html', {'form': form})
    else:
        form    = Registreeform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Applicant Sucessfully Registered')
        return render(request, 'homepages/user/guest_user_menu.html', {'content':content})
    else:
        args['form'] = form
        return render(request, 'homepages/user/menu-page/application_form.html', {'form': form})

#add New Student Registration Form
#login_required(login_url='login')
#allowed_users(allowed_roles=['registrar', 'admin','student'])
def new_student_appform(request):
    args = {}
    if request.method == "GET":
        form    = Prospectform()
        return render(request, 'homepages/registrar/manage_enrollment/registree/new_student_appform.html', {'form': form})
    else:
        form    = Prospectform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Student Application Sucessfully Registered')
        new_student_appform = Prospect.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/registree/new_student_appform.html', {'new_student_appform':new_student_appform})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/registree/new_student_appform.html', {'form': form})

#Re-Apply Student Application Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin','student'])
def xstudent_application(request):
    args = {}
    if request.method == "GET":
        form    = Studentform()
        return render(request, 'homepages/student/re-enroll/xstudent_application.html', {'form': form})
    else:
        form    = Studentform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Applicant Sucessfully Registered')
        student  = Student.objects.all()
        return render(request, 'homepages/student/student_menu.html', {'student': student})
    else:
        args['form'] = form
        return render(request, 'homepages/student/re-enroll/xstudent_application.html', {'form': form})


#Re-Apply Student Application Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin','student'])
def xstudent_application2(request):
    args = {}
    if request.method == "GET":
        form    = Studentform()
        return render(request, 'homepages/student/re-enroll/xstudent_application2.html', {'form': form})
    else:
        form    = Studentform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Applicant Sucessfully Registered')
        student  = Student.objects.all()
        return render(request, 'homepages/registrar/registrar_menu.html', {'student': student})
    else:
        args['form'] = form
        return render(request, 'homepages/student/re-enroll/xstudent_application2.html', {'form': form})

#View Existing Student Enrollment
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar', 'student'])
def xstudent_view(request):
    student = Student.objects.all()
    return render(request, 'homepages/student/re-enroll/xstudent_view.html', {'student': student})

#View Each Existing Student
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_xstudent(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'homepages/student/re-enroll/view_xstudent.html', {'student': student})

#Update Existing Student
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_xstudent(request, student_id=0):
    args = {}
    if request.method == "GET":
        if student_id==0:
            form    = updatestudentform()
        else: 
            student  = Student.objects.get(pk=student_id)
            form    = updatestudentform(instance=student)
        return render(request, 'homepages/student/re-enroll/update_xstudent.html', {'form': form})
    else:
        if student_id==0:
            form    = updatestudentform(request.POST)
        else:
            student  =  Student.objects.get(pk=student_id)
            form    =  updatestudentform(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Sucessfully Updated')
            student = Student.objects.all()
            return render(request, 'homepages/student/re-enroll/xstudent_view.html.html', {'student': student})
        else:
            args['form'] = form
            return render(request, 'homepages/student/re-enroll/update_xstudent.html', {'form': form})
   
    
#add Exam Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def exam_form(request):
    args = {}
    if request.method == "GET":
        form    = Entrance_Examform()
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entrance_exam.html', {'form': form})
    else:
        form    = Entrance_Examform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Exam Attributes Sucessfully Registered')
        entr_xview  = Entrance_Exam.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entr_xview.html', {'entr_xview': entr_xview})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entrance_exam.html', {'form': form})

#add Enroll Exam Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def enroll_xform(request):
    args = {}
    if request.method == "GET":
        form    = Enroll_Examform()
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xform.html', {'form': form})
    else:
        form    = Enroll_Examform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Exam Attributes Sucessfully Registered')
        enroll_xview  = Enroll_Exam.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xview.html', {'enroll_xview': enroll_xview})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xform.html', {'form': form})

#add Exam Status Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def stats_xform(request):
    args = {}
    exam_stats = Exam_Stats.objects.all()
    exam_card = Enroll_Exam.objects.all()
    if request.method == "GET":
        form    = Exam_Statsform()
        context = {
            'form' : form,
            'exam_stats' : exam_stats,
            'exam_card' : exam_card
        }
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xform.html', context)
    else:
        form    = Exam_Statsform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Exam Result Sucessfully Registered')
        form = Exam_Stats()
        exam_stats = Exam_Stats.objects.all()
        context = {
            'form' : form,
            'exam_stats' : exam_stats
        }
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xview.html', context)
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xform.html', {'form': form})

# ---------------------------------------------------- Classroom Management ------------------------------------------------------------------
#add Subject Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def subject_form(request):
    args = {}
    if request.method == "GET":
        form    = Subjectform()
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_form.html', {'form': form})
    else:
        form    = Subjectform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Subject Assignment Sucessfully Registered')
        subj_view  = Subject.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_view.html', {'subj_view': subj_view})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_form.html', {'form': form})

#add Class Assignment Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def classr_form(request):
    args = {}
    if request.method == "GET":
        form    = Classroomform()
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_form.html', {'form': form})
    else:
        form    = Classroomform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Classroom Assignment Sucessfully Registered')
        classr_view  = Classroom.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_view.html', {'classr_view': classr_view})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_form.html', {'form': form})

#add Class Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def class_form(request):
    args = {}
    assign_class = Classroom.objects.all()
    hr_teacher = Teacher.objects.all()
    if request.method == "GET":
        form    = Assign_Classform()
        context = {
            'form' : form,
            'assign_class' : assign_class,
            'hr_teacher' : hr_teacher
        }
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/class_form.html', context)
    else:
        form    = Assign_Classform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Class Added Sucessfully')
        form = Assign_Class()
        assign_class = Assign_Class.objects.all()
        context = {
            'form' : form,
            'assign_class' : assign_class
        }
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/class_form.html', context)
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/class_form.html', {'form': form})

#add Teacher Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def teacher_form(request):
    args = {}
    if request.method == "GET":
        form    = Teacherform()
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_form.html', {'form': form})
    else:
        form    = Teacherform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Teacher Assignment Sucessfully Registered')
        teacher  = Teacher.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_view.html', {'teacher': teacher})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_form.html', {'form': form})

#add Staffs Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def staffs_form(request):
    args = {}
    if request.method == "GET":
        form    = Staffform()
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_form.html', {'form': form})
    else:
        form    = Staffform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Staff Assignment Sucessfully Registered')
        staff  = Staff.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staffs_view.html', {'staff': staff})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staff_form.html', {'form': form})
  
 
#View Applicant
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_applicants(request):
    applicant = Registree.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/registree/applicant_view.html', {'applicant': applicant})

#View Prospect
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_prospect(request):
    prospect = Prospect.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/registree/view_prospect.html', {'prospect': prospect})

#View Each Prospect
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_prospect(request, pros_id):
    prospect = Prospect.objects.get(pk=pros_id)
    return render(request, 'homepages/registrar/manage_enrollment/registree/view_each_prospect.html', {'prospect': prospect})

#View Each Registree
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar'])
def view_each_registree(request, regis_id):
    registree_each = Registree.objects.get(pk=regis_id)
    return render(request, 'homepages/manage_enrollment/registree/view_each_registree.html', {'registree_each': registree_each}) 


#View Entrance Exam Attributes
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def entr_xview(request):
    entr_xview = Entrance_Exam.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/entr_xview.html', {'entr_xview': entr_xview})

#View Enroll Exam Attributes
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def enroll_xview(request):
    enroll_xview = Enroll_Exam.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/enroll_xview.html', {'enroll_xview': enroll_xview})

#View Each Enroll Examinee Attributes
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_examinee(request, enroll_xview_id):
    enroll_xview = Enroll_Exam.objects.get(pk=enroll_xview_id)
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/view_each_examinee.html', {'enroll_xview': enroll_xview})

#View Exam Status
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def stats_xview(request):
    exam_stats = Exam_Stats.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/stats_xview.html', {'exam_stats': exam_stats})

#View Each Exam Status
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_xstats(request, exam_stats_id):
    exam_stats = Exam_Stats.objects.get(pk=exam_stats_id)
    return render(request, 'homepages/registrar/manage_enrollment/entrance_exam/view_each_xstats.html', {'exam_stats': exam_stats})

#View Subject Assigned
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def subj_view(request):
    subj_view = Subject.objects.all().order_by('-grade_level')
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/subject_view.html', {'subj_view': subj_view})

#View Each Class Subject
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar'])
def view_class_subject(request, class_sbj_id):
    subj_view = Subject.objects.get(pk=class_sbj_id)
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/view_class_subject.html', {'subj_view': subj_view}) 

#View Assigned Class
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def classr_view(request):
    classr_view = Classroom.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/classr_view.html', {'classr_view': classr_view})

#View Each Assigned Class
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_class_room(request, classr_view_id):
    classr_view = Classroom.objects.get(pk=classr_view_id)
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/view_class_room.html', {'classr_view': classr_view})

#View Classroom
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def assigned_class(request):
    assigned_class = Assign_Class.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class.html', {'assigned_class': assigned_class})

#View Each Classroom
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def assigned_class_view(request, assigned_class_id):
    assigned_class = Assign_Class.objects.get(pk=assigned_class_id)
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class_view.html', {'assigned_class': assigned_class})

#Assigned Class Management
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def asgclass_management(request):
    assigned_class = Assign_Class.objects.all()
    asgclassFilter = AsgclassFilter(request.GET, queryset=assigned_class)
    assigned_class = asgclassFilter.qs
    
    context = {
        'assigned_class':assigned_class,
        'asgclassFilter': asgclassFilter
    }
    return render(request, 'homepages/registrar/manage_enrollment/class_enrollment/assigned_class.html', context)


# ---------------------------------------------------------------- Staff Management --------------------------------------------------------------
#View Teacher
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def teacher_view(request):
    teacher = Teacher.objects.all().order_by('-date_joined')
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_view.html', {'teacher': teacher})

#View Each Teacher
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/view_each_teacher.html', {'teacher': teacher})

#Teacher Management
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def teacher_management(request):
    teacher = Teacher.objects.all().order_by('date_joined')
    if 'q' in request.GET:
        q =request.GET['q']
        teacher = Teacher.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(email__icontains=q)|Q(phone_num__icontains=q))
    teacher_count = teacher.count()
    
    context = {
        'teacher':teacher,
        'teacher_count': teacher_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/teacher_view.html', context)

#View Staff
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def staffs_view(request):
    staff = Staff.objects.all().order_by('-date_added')
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staffs_view.html', {'staff': staff})

#View Each Staff
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_each_staff(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/view_each_staff.html', {'staff': staff})

#Staff Management
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def staff_management(request):
    staff = Staff.objects.all().order_by('-date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        staff = Staff.objects.filter(Q(card_number__icontains=q)|Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(contact__icontains=q))
    staff_count = staff.count()
    
    context = {
        'staff':staff,
        'staff_count': staff_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/staffs_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_staff_user(request):
    staff = Staff.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/staff_enrollment/view_staff_user.html', {'staff': staff})


# ---------------------------------------------------------------- Staff User Management --------------------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def staff_users_view(request):
    staff_user = Staff_User.objects.all()
    return render(request, 'homepages/admin/user_management/users/staff_users_view.html', {'staff_user': staff_user})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def staff_user_view(request, staff_user_id):
    staff_user = Staff_User.objects.get(pk=staff_user_id)
    return render(request, 'homepages/admin/user_management/users/staff_user_view.html', {'staff_user': staff_user})

#Staff Management
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def staff_user_management(request):
    staff_user = Staff_User.objects.all()
    staffUserFilter = StaffUserFilter(request.GET, queryset=staff_user)
    staff_user = staffUserFilter.qs
    
    context = {
        'staff_user':staff_user,
        'staffUserFilter': staffUserFilter
    }
    return render(request, 'homepages/admin/user_management/users/staff_user_view.html', context)

# ---------------------------------------------------------------- New Student Management --------------------------------------------------------------

#New Student Enrollment Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def enroll_nstudent(request):
    args = {}
    exam_card = Exam_Stats.objects.all()
    into_class = Enroll_NStudent.objects.all()
    if request.method == "GET":
        form    = Enroll_NStudentform()
        context = {
            'form' : form,
            'exam_card' : exam_card,
            'into_class' : into_class
        }
        return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_form.html', context)
    else:
        form    = Enroll_NStudentform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Student Enrolled Sucessfully')
        form = Enroll_NStudent()
        nstudent = Enroll_NStudent.objects.all()
        context = {
            'form' : form,
            'nstudent' : nstudent
        }
        return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_view.html', context)
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_form.html', {'form': form})

#Update New Student Information
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def update_nstudent(request, nstudent_id=0):
    args = {}
    if request.method == "GET":
        if nstudent_id==0:
            form    = updateenroll_nstudentform()
        else: 
            nstudent  = Enroll_NStudent.objects.get(pk=nstudent_id)
            form    = updateenroll_nstudentform(instance=nstudent)
        return render(request, 'homepages/registrar/manage_enrollment/student_info/update_nstudent.html', {'form': form})
    else:
        if nstudent_id==0:
            form    = updateenroll_nstudentform(request.POST)
        else:
            nstudent  =  Enroll_NStudent.objects.get(pk=nstudent_id)
            form    =  updateenroll_nstudentform(request.POST, request.FILES, instance=nstudent)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Student Sucessfully Updated')
            nstudent = Enroll_NStudent.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_view.html', {'nstudent': nstudent})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/student_info/update_nstudent.html', {'form': form})

#View New Student Enrollment
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def enroll_nstudent_view(request):
    nstudent = Enroll_NStudent.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_view.html', {'nstudent': nstudent})

#View Each New Student Enrollment
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def view_nstudent(request, nstudent_id):
    nstudent = Enroll_NStudent.objects.get(pk=nstudent_id)
    return render(request, 'homepages/registrar/manage_enrollment/student_info/view_nstudent.html', {'nstudent': nstudent})

#New Student Management
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def nstudent_management(request):
    nstudent =Enroll_NStudent.objects.all().order_by('date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        nstudent = Enroll_NStudent.objects.filter(Q(student_user__username__icontains=q)|Q(examid_card__exam_card__prospect_name__first_name__icontains=q)
                                                  |Q(examid_card__exam_card__prospect_name__first_name__icontains=q)|Q(into_class__class_level__icontains=q))
    nstudentusr_count = nstudent.count()
    
    context = {
        'nstudent':nstudent,
        'nstudentusr_count' : nstudentusr_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/student_info/enroll_nstudent_view.html', context)


#-------------------------------------------------------- Add Class by Academic Year -------------------------------------------------------------

#Add Class by Academic Year Form
@login_required(login_url='login')
@allowed_users(allowed_roles=['registrar', 'admin'])
def class_academic(request):
    args = {}
    if request.method == "GET":
        form    = Class_Academicform()
        return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic.html', {'form': form})
    else:
        form    = Class_Academicform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Classroom by Academic Year Sucessfully Registered')
        class_academic  = Class_Academic.objects.all()
        return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_list.html', {'class_academic': class_academic})
    else:
        args['form'] = form
        return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic.html', {'form': form})

#Classroom by Academic Year
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def class_academic_management(request):
    class_academic = Class_Academic.objects.all().order_by('date_added')
    if 'q' in request.GET:
        q =request.GET['q']
        class_academic = Class_Academic.objects.filter(Q(student_class__first_name__icontains=q)|Q(student_class__first_name__icontains=q)
                                                        |Q(student_class__user__username__icontains=q)
                                                        |Q(class_academic__class_level__icontains=q))
    class_academic_count = class_academic.count()
    
    context = {
        'class_academic':class_academic,
        'class_academic_count': class_academic_count
    }
    return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_list.html', context)

#Update Classroom by Academic Year
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def class_academic_update(request, class_academic_id=0):
    args = {}
    if request.method == "GET":
        if class_academic_id==0:
            form    = Class_Academicform()
        else: 
            class_academic  = Class_Academic.objects.get(pk=class_academic_id)
            form    = updateclass_academicform(instance=class_academic)
        return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_update.html', {'form': form})
    else:
        if class_academic_id==0:
            form    = updateclass_academicform(request.POST)
        else:
            class_academic  =  Class_Academic.objects.get(pk=class_academic_id)
            form    =  updateclass_academicform(request.POST, request.FILES, instance=class_academic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class by Academic Year Sucessfully Updated')
            class_academic = Class_Academic.objects.all()
            return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_list.html', {'class_academic': class_academic})
        else:
            args['form'] = form
            return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_update.html', {'form': form})


#List Classroom by Academic Year
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def class_academic_list(request, classr_view_id=0):
    class_academic = Enroll_NStudent.objects.get(pk=classr_view_id)
    return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_list.html', {'class_academic': class_academic})


#View Each Class by Academic Year
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'registrar'])
def class_academic_view(request, class_academic_id):
    class_academic = Enroll_NStudent.objects.get(pk=class_academic_id)
    return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_view.html', {'class_academic': class_academic})

#Admin Delete Classroom by Academic Year
def class_academic_delete(request, class_academic_id=0):
    class_academic = Class_Academic.objects.get(pk=class_academic_id)
    class_academic.delete()
    class_academic = Class_Academic.objects.all()
    return render(request, 'homepages/registrar/manage_enrollment/class_academic/class_academic_list.html', {'class_academic': class_academic})



def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'users/partials/state_dropdown_list_options.html', {'states': states})


def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'users/partials/city_dropdown_list_options.html', {'cities': cities})


def load_streets(request):
    city_id = request.GET.get('city')
    streets = Street.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'users/partials/street_dropdown_list_options.html', {'streets': streets}) 
#--------------------------------------------------------END---------------------------------------------------------------------------------

#Sending Email
def send_email(request):
    if request.method=="POST":
        email_id = request.POST.get('email_id')
        response_data = "email send to "+email_id
        email_name = email_id.split('@')

        email_template = render_to_string(
            'homepages/admin/account_management/message-center/message.html', {"username": email_name[0]})
        email_obj = EmailMultiAlternatives(
            "dekocsl@gmail.com",
            "selita9801@gmail.com",
            settings.EMAIL_HOST_USER,
            [email_id],
        )
        email_obj.attach_alternative(email_template, 'text/html')
        email_obj.send()
        context = {"data":response_data}
        return render(request,"homepages/admin/account_management/message-center/contact_form.html",context)
    else:
        context = {"data":"response_data"}
        return render(request,"homepages/admin/account_management/message-center/contact_form.html")

#-----------------Logout Request
def signout(request):
	logout(request)
	return redirect('/')



#--------------------------------------------------------END---------------------------------------------------------------------------------
