from django.urls import URLPattern, path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.loginpage),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('import/', views.importExcel, name="push_excel"),
        
    
   #View User_View
    path('view_groups/', views.view_groups, name="view_groups"),
    path('view_users/', views.view_users, name="view_users"),
    path('view_guest/', views.view_guest, name="view_guest"),
    
    
    #Users_Management
    #path('create_user', views.create_user, name='create_user'),
    path('update_user/?P<int:user_id>/',views.update_user, name="update_user"),
    path('update_user_password/?P<int:password_id>/',views.update_user_password, name="update_user_password"),
    path('delete_user/?P<int:user_id>/', views.delete_user, name="delete_user"),
    path('user_management/', views.user_management, name="user_management"),
      
    #Create Admin_User_Creation
    path('admin_menu/', views.admin_menu, name="admin_menu"),
    path('create_admin_user/', views.create_admin_user, name="create_admin_user"),
    path('view_admin/', views.view_admin, name="view_admin"),
    path('update_admin_user/?P<int:admin_id>/', views.update_admin_user, name="update_admin_user"),
    path('delete_student/?P<int:admin_id>/', views.delete_student, name="delete_student"),
    re_path(r'^admin_change_password/$', views.admin_change_password, name='admin_change_password'),
    path('admin_user_management/', views.admin_user_management, name="admin_user_management"),
    path('admin_profile/?P<int:admin_id>/', views.admin_profile, name="admin_profile"),
    
    
    #Create Student_User_Creation
    path('student_menu/', views.student_menu, name="student_menu"),
    path('create_student_user/', views.create_student_user, name="create_student_user"),
    path('view_student/', views.view_student, name="view_student"),
    path('view_each_student/?P<int:student_id>/', views.view_each_student, name="view_each_student"),
    path('update_student_user/?P<int:student_id>/', views.update_student_user, name="update_student_user"),
    path('update_student_password/?P<int:password_id>/', views.update_student_password, name="update_student_password"),
    re_path(r'^change_student_password/$', views.change_student_password, name='change_student_password'),
    path('delete_student/?P<int:student_id>/', views.delete_student, name="delete_student"),
    #path('student_user_management/', views.student_user_management, name="student_user_management"),
    #path('student_user_profile/?P<int:student_id>/', views.student_user_profile, name="student_user_profile"),
    
    #Create Registrar_User_Creation
    path('registrar_menu/', views.registrar_menu, name="registrar_menu"),
    path('create_registrar_user/', views.create_registrar_user, name="create_registrar_user"),
    path('view_registrar_user/', views.view_registrar_user, name="view_registrar_user"),
    path('update_registrar_user/', views.update_registrar_user, name="update_registrar_user"),
    path('update_registrar_password/', views.update_registrar_password, name="update_registrar_password"),
    re_path(r'^password2/$', views.change_password2, name='change_password2'),
    path('delete_registrar/?P<int:registrar_id>/', views.delete_registrar, name="delete_registrar"),
    #path('registrar_user_management/', views.registrar_user_management, name="registrar_user_management"),   
    #path('registrar_user_profile/?P<int:registrar_id>/', views.registrar_user_profile, name="registrar_user_profile"), 
    
    
    #Create Staff_User_Creation
    #path('staff_menu/', views.staff_menu, name="staff_menu"),
    path('create_staff_user/', views.create_staff_user, name="create_staff_user"),
    path('view_staff_user/', views.view_staff_user, name="view_staff_user"),
    path('staff_user_view/?P<int:staff_user_id>/', views.staff_user_view, name="staff_user_view"),
    path('staff_users_view/', views.staff_users_view, name="staff_users_view"),
    path('update_staff_user/?P<int:staff_user_id>/', views.update_staff_user, name="update_staff_user"),
    #path('update_staff_password/', views.update_staff_password, name="update_staff_password"),
    re_path(r'^password2/$', views.change_password2, name='change_password2'),
    path('delete_staff_user/?P<int:staff_user_id>/', views.delete_staff_user, name="delete_staff_user"),
    path('staff_user_management/', views.staff_user_management, name="staff_user_management"),
    #path('staff_user_profile/?P<int:staff_id>/', views.staff_user_profile, name="staff_user_profile"), 
    
    
    #Create Guest_User
    path('guest_user_menu/', views.guest_user_menu, name="guest_user_menu"),
    path('create_guest_user/', views.create_guest_user, name="create_guest_user"),
    path('update_guest_user/', views.update_guest_user, name="update_guest_user"),

    
    #path('registrar_profile/?P<int:registrar_id>/', views.registrar_profile, name="registrar_profile"),
    
    #Delete Functions
    path('delete_class_sbj/?P<int:class_sbj_id>/', views.delete_class_sbj, name="delete_class_sbj"),
    path('delete_classroom/?P<int:classr_view_id>/', views.delete_classroom, name="delete_classroom"),
    path('delete_assigned_class/?P<int:assigned_class_id>/', views.delete_assigned_class, name="delete_assigned_class"),
    
    #Update Functions
    
    path('change_password1/', views.change_password1, name="change_password1"),
    
    #path('view_registration/', views.view_registration, name="view_registration"),
    #path('student_registration/', views.student_registration, name="student_registration"),
    
        
    ###################################################Entrance Exam Attributes
    
    #Prospect Management
    #path('prospect_form/', views.prospect_form, name="prospect_form"),
    path('view_prospect/', views.view_prospect, name="view_prospect"),
    path('view_each_prospect/?P<int:pros_id>/', views.view_each_prospect, name="view_each_prospect"),
    path('update_prospect/?P<int:pros_id>/', views.update_prospect, name="update_prospect"),
    #path('delete_prospect/?P<int:pros_id>/', views.delete_prospect, name="delete_edelete_prospectntr_exam"),
    path('prospect_management/', views.prospect_management, name="prospect_management"),
    
    #Exam Form Management
    path('exam_form/', views.exam_form, name="exam_form"),
    path('entr_xview/', views.entr_xview, name="entr_xview"),
    path('update_entrancex/?P<int:entr_exam_id>/', views.update_entrancex, name="update_entrancex"),
    path('delete_entr_exam/?P<int:entr_exam_id>/', views.delete_entr_exam, name="delete_entr_exam"),
    path('entr_management/', views.entr_management, name="entr_management"),
    
    #Enroll Exam Form Management    
    path('enroll_xform/', views.enroll_xform, name="enroll_xform"),
    path('enroll_xview/', views.enroll_xview, name="enroll_xview"),
    path('view_each_examinee/?P<int:enroll_xview_id>/', views.view_each_examinee, name="view_each_examinee"),
    path('update_xenroll/?P<int:enroll_xview_id>/', views.update_xenroll, name="update_xenroll"),
    #path('delete_examinee_exam/?P<int:enroll_xview_id>/', views.delete_entr_exam, name="delete_entr_exam"),
    path('xview_management/', views.xview_management, name="xview_management"),
    
    #Result or Status of Exam Form Management
    path('stats_xform/', views.stats_xform, name="stats_xform"),
    path('stats_xview/', views.stats_xview, name="stats_xview"),
    path('view_each_xstats/?P<int:exam_stats_id>/', views.view_each_xstats, name="view_each_xstats"),
    path('update_statsx/?P<int:exam_stats_id>/', views.update_statsx, name="update_statsx"),
    #path('delete_xstats_exam/?P<int:exam_stats_id>/', views.delete_xstats_exam, name="delete_xstats_exam"),
    path('xstats_management/', views.xstats_management, name="xstats_management"),
    
    #################################################Class Enrollment Attributes
    #Classroom - Subject Mangement
    path('subject_form/', views.subject_form, name="subject_form"),
    path('subj_view/', views.subj_view, name="subj_view"),
    path('view_class_subject/?P<int:class_sbj_id>/', views.view_class_subject, name="view_class_subject"),
    path('update_subject/?P<int:class_sbj_id>/', views.update_subject, name="update_subject"),
    #path('delete_subject/?P<int:class_sbj_id>/', views.delete_subject, name="delete_subject"),
    path('subject_management/', views.subject_management, name="subject_management"),
    
    #Classroom - Classroom Management
    path('classr_form/', views.classr_form, name="classr_form"),
    path('classr_view/', views.classr_view, name="classr_view"),
    path('view_class_room/?P<int:classr_view_id>/', views.view_class_room, name="view_class_room"),
    path('update_classr/?P<int:classr_view_id>/', views.update_classr, name="update_classr"),
    #path('delete_classr/?P<int:classr_view_id>/', views.delete_classr, name="delete_classr"),
    path('classr_management/', views.classr_management, name="classr_management"),
    
    #Classroom - Class Management
    path('class_form/', views.class_form, name="class_form"),
    path('assigned_class/', views.assigned_class, name="assigned_class"),
    path('assigned_class_view/?P<int:assigned_class_id>/', views.assigned_class_view, name="assigned_class_view"),
    path('update_assigned_class/?P<int:assigned_class_id>/', views.update_assigned_class, name="update_assigned_class"),
    #path('delete_asgclass/?P<int:assigned_class_id>/', views.delete_asgclass, name="delete_asgclass"),
    path('asgclass_management/', views.asgclass_management, name="asgclass_management"),
    
    
    
    #################################################Staff Management Attributes
    #Teacher Management 
    path('teacher_form/', views.teacher_form, name="teacher_form"),
    path('teacher_view/', views.teacher_view, name="teacher_view"),
    path('view_each_teacher/?P<int:teacher_id>/', views.view_each_teacher, name="view_each_teacher"),
    path('update_teacher/?P<int:teacher_id>/', views.update_teacher, name="update_teacher"),
    #path('delete_teacher/?P<int:teacher_id>/', views.delete_teacher, name="delete_teacher"),
    path('teacher_management/', views.teacher_management, name="teacher_management"),
    
    
    #Staff/s Management 
    path('staffs_form/', views.staffs_form, name="staffs_form"),
    path('staffs_view/', views.staffs_view, name="staffs_view"),
    
    path('staff_form/', views.staff_form, name="staff_form"),
    path('staff_view/', views.staff_view, name="staff_view"),
    path('view_each_staff/?P<int:staff_id>/', views.view_each_staff, name="view_each_staff"),
    path('update_staff/?P<int:staff_id>/', views.update_staff, name="update_staff"),
    path('delete_staff/?P<int:staff_id>/', views.delete_staff, name="delete_staff"),
    path('staff_management/', views.staff_management, name="staff_management"),
    
    
    #############################################Manage Enrollment Process
    path('application_form/', views.application_form, name="application_form"),
    path('new_student_appform/', views.new_student_appform, name="new_student_appform"),
    
    #Existing Student Management
    path('xstudent_application/', views.xstudent_application, name="xstudent_application"),
    path('xstudent_application2/', views.xstudent_application2, name="xstudent_application2"),
    path('xstudent_view/', views.xstudent_view, name="xstudent_view"),
    path('view_xstudent/?P<int:student_id>/', views.view_xstudent, name="view_xstudent"),
    path('update_xstudent/?P<int:student_id>/', views.update_xstudent, name="update_xstudent"),
    path('delete_xstudent/?P<int:student_id>/', views.delete_xstudent, name="delete_xstudent"),
    path('xstudent_management/', views.xstudent_management, name="xstudent_management"),
    
    path('view_applicants/', views.view_applicants, name="view_applicants"),
    
    #New Student Management
    path('view_each_registree/', views.view_each_registree, name="view_each_registree"),
    path('enroll_nstudent/', views.enroll_nstudent, name="enroll_nstudent"),
    path('enroll_nstudent_view/', views.enroll_nstudent_view, name="enroll_nstudent_view"),
    path('update_nstudent/?P<int:nstudent_id>/', views.update_nstudent, name="update_nstudent"),
    path('view_nstudent/?P<int:nstudent_id>/', views.view_nstudent, name="view_nstudent"),
    path('nstudent_management/', views.nstudent_management, name="nstudent_management"),
    
    #Class Academic Managemetn
    path('class_academic/', views.class_academic, name="class_academic"),
    path('class_academic_list/', views.class_academic_list, name="class_academic_list"),
    path('class_academic_view/?P<int:class_academic_id>/', views.class_academic_view, name="class_academic_view"),
    path('class_academic_update/?P<int:class_academic_id>/', views.class_academic_update, name="class_academic_update"),
    path('class_academic_delete/?P<int:class_academic_id>/', views.class_academic_delete, name="class_academic_delete"),
    path('class_academic_management/', views.class_academic_management, name="class_academic_management"),
    
    
    #path('enrollment_form/', views.enrollment_form, name="enrollment_form"),
    #path('view_enrollment/', views.view_enrollment, name="view_enrollment"),
    
    #path('open/<str:path>/', views.open_file, name='open-file'),
    path("send_email/",views.send_email, name="send_email"),
    
    
    
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-streets/', views.load_streets, name='ajax_load_streets'),
    #-------------------- Logout Request -----------------------------------
    path('signout', views.signout, name="signout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)