from django.contrib import admin
# Register your models here.
from .models import *

class Academic_YearAdmin(admin.ModelAdmin):
    search_fields=('start_end_year',)
    list_display=('start_end_year', 'academic_year', 'date_added')
    
class RegistreeAdmin(admin.ModelAdmin):
    search_fields=('last_name',)
    list_display=('last_name', 'first_name', 'gender', 'grade_level', 'parent_contact', 'parent_email', 'date_added',)

class ProspectAdmin(admin.ModelAdmin):
    search_fields=('first_name',)
    list_display=('first_name', 'last_name', 'gender', 'apply_grade_level', 'vaccinated', 'emergency_cont_name', 'emergency_contact', 'parent_name', 'date_added',)
    
class TeacherAdmin(admin.ModelAdmin):
    search_fields=('staff_user',)
    list_display=('staff_user', 'first_name', 'last_name', 'nationality', 'religion', 'profile_pic', 'bachelor_degree', 'email', 'phone_num', 'date_joined',)

class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_idcard',)
    list_display=('student_idcard','user' ,'first_name', 'last_name', 'gender', 'grade_level', 'email', 'parent_contact1', 'address', 'date_joined',)

class StaffAdmin(admin.ModelAdmin):
    search_fields=('user',)
    list_display=('user', 'card_number', 'first_name', 'last_name', 'gender', 'position', 'status', 'contact', 'profile_pic', 'date_added')

class Staff_UserAdmin(admin.ModelAdmin):
    search_fields=('username',)
    list_display=('username', 'card_number', 'date_added')
     
class Entrance_ExamAdmin(admin.ModelAdmin):
    search_fields=('class_name',)
    list_display=('class_name', 'class_building', 'time_schedule', 'date_exam',)
    
class Enroll_ExamAdmin(admin.ModelAdmin):
    search_fields=('prospect_name',)
    list_display=('prospect_name', 'username', 'classroom', 'date_added') 

class Exam_StatsAdmin(admin.ModelAdmin):
    search_fields=('exam_card',)
    list_display=('exam_card', 'exam_type', 'exam_status', 'exam_score', 'date_added') 
   
class ClassroomAdmin(admin.ModelAdmin):
    search_fields=('class_level',)
    list_display=('class_level', 'subject', 'class_bld', 'class_capacity', 'date_added') 
        
class SubjectAdmin(admin.ModelAdmin):
    search_fields=('class_subject',)
    list_display=('class_subject', 'grade_level', 'date_added')
    
class Class_AcademicAdmin(admin.ModelAdmin):
    search_fields=('class_academic',)
    list_display=('class_academic', 'student_class', 'date_added') 
     
class Enroll_NStudentAdmin(admin.ModelAdmin):
    search_fields=('into_class',)
    list_display=('into_class', 'examid_card', 'student_user', 'academic_year', 'date_added') 


admin.site.register(Academic_Year, Academic_YearAdmin)        
admin.site.register(Registree, RegistreeAdmin)
admin.site.register(Prospect, ProspectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Staff_User, Staff_UserAdmin)

admin.site.register(Entrance_Exam, Entrance_ExamAdmin)
admin.site.register(Enroll_Exam, Enroll_ExamAdmin)
admin.site.register(Exam_Stats, Exam_StatsAdmin)

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enroll_NStudent, Enroll_NStudentAdmin)
admin.site.register(Class_Academic, Class_AcademicAdmin)
