import django_filters

from .models import *

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'groups']
        
class ProspectFilter(django_filters.FilterSet):
    class Meta:
        model = Prospect
        fields = ['first_name', 'apply_grade_level', 'academic_year']

class XviewFilter(django_filters.FilterSet):
    class Meta:
        model = Enroll_Exam
        fields = ['prospect_name', 'username', 'classroom']
        
class XstatsFilter(django_filters.FilterSet):
    class Meta:
        model = Exam_Stats
        fields = ['exam_card', 'exam_status', 'exam_type']
        
class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = ['grade_level']
        
class ClassrFilter(django_filters.FilterSet):
    class Meta:
        model = Classroom
        fields = ['class_level', 'class_bld']        
             
       
class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['bachelor_degree']
             
class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['user', 'card_number', 'first_name', 'position', 'status']
 
class StaffUserFilter(django_filters.FilterSet):
    class Meta:
        model = Staff_User
        fields = ['username', 'card_number']
               
class NstudentFilter(django_filters.FilterSet):
    class Meta:
        model = Enroll_NStudent
        fields = ['student_user', 'examid_card', 'into_class', 'academic_year', 'into_class']
        