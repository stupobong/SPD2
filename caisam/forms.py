from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from caisam.models import *
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from django.contrib import admin
from django_select2.forms import ModelSelect2Widget, Select2Widget



class userform(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'email_exist':_("A user with that email already exists.")

    }
    
    password1 = forms.CharField(label=_("New Password"),
        widget=forms.PasswordInput,
        help_text=_("<ul><li>Your password can't be too similar to your other personal information.</li>"
                    "<li>Your password must contain at least 8 characters.</li>"
                    "<li>Your password can't be a commonly used password.</li>"
                    "<li>Your password can't be entirely numeric.</li></ul>"))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput)

    class Meta:
        model   = User
        fields  = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels  = {
            
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            }

    def clean_email(self):
            email= self.cleaned_data.get('email')
            if email and User.objects.filter(email=email):
                raise forms.ValidationError(
                self.error_messages['email_exist'],
                code='email_exist',
            )
            return email
            
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(userform, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class updateuserform(forms.ModelForm):
    
    class Meta:
        model   = User
        fields  = ['username', 'email', 'first_name', 'last_name', 'groups', 'is_active']
        labels  = {
            
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'groups' : 'groups',
            'is_active' : 'Active'
            }

class updatepassword(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("New Password"),
        widget=forms.PasswordInput,
        help_text=_("<ul><li>Your password can't be too similar to your other personal information.</li> "
                    "<li>Your password must contain at least 8 characters.</li>"
                    "<li>Your password can't be a commonly used password.</li>"
                    "<li>Your password can't be entirely numeric.</li></ul>"))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput)

    class Meta:
        model   = User
        fields  = ['password1', 'password2']
        labels  = {
            
                    'password1' : 'New Password',
                    'password2' : 'Confirmation Password'
                }
                

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(updatepassword, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Academic_YearForm(forms.ModelForm):
    class Meta:
        model = Academic_Year
        fields = ['academic_year', 'start_end_year']
        labels = { 
                    'academic_year' : 'Academic Year', 
                    'start_end_year' : 'Academic Year Started to End', 
                }        
class UpdateAcademic_YearForm(forms.ModelForm):
    class Meta:
        model = Academic_Year
        fields = ['academic_year', 'start_end_year']
        labels = { 
                    'academic_year' : 'Academic Year', 
                    'start_end_year' : 'Academic Year Started to End', 
                }

class Registreeform(forms.ModelForm):
    
    class Meta:
        model   = Registree
        fields  = ['first_name', 'last_name', 'gender', 'DoB', 'nationality', 'religion', 'grade_level', 'academic_year', 
                   'parent_name', 'parent_occupation', 'parent_email', 'parent_contact',
                   'address', 'city', 'country', 'profile_pic']
        labels  = { 
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'DoB' : 'Date of Birth', 
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'grade_level' : 'Grade Level',
                    'academic_year' : 'Academic Year',
                    
                    'parent_name' : 'Parent Name', 
                    'parent_occupation' : 'Parent Occupation/Job', 
                    'parent_email' : 'Parent Email', 
                    'parent_contact' : 'Parent Phone Contact', 
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident',
                    'profile_pic' : 'Profile Picture'
                }        
class updateregistreeform(forms.ModelForm):
    
    class Meta:
        model   = Registree
        fields  = ['first_name', 'last_name', 'gender', 'DoB', 'nationality', 'religion', 'grade_level', 'academic_year', 
                   'parent_name', 'parent_occupation', 'parent_email', 'parent_contact',
                   'address', 'city', 'country', 'profile_pic']
        labels  = { 
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'DoB' : 'Date of Birth', 
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'grade_level' : 'Grade Level',
                    'academic_year' : 'Academic Year',
                    
                    'parent_name' : 'Parent Name', 
                    'parent_occupation' : 'Parent Occupation/Job', 
                    'parent_email' : 'Parent Email', 
                    'parent_contact' : 'Parent Phone Contact', 
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident',
                    'profile_pic' : 'Profile Picture'
                }

class Prospectform(forms.ModelForm):
    
    class Meta:
        model   = Prospect
        fields  = ['first_name', 'last_name', 'gender', 'DoB', 'birth_address','nationality', 'religion', 'apply_grade_level', 'academic_year', 'profile_pic',
                   'health_record', 'physical_checkup', 'vaccinated', 'dose_vaccination', 'id_vaccine_card', 'early_school', 
                   'parent_name', 'parent_occupation', 'parent_email', 'parent_contact', 'emergency_cont_name', 'emergency_contact', 'emergency_address', 
                   'address', 'city', 'country', 'profile_pic']
        labels  = { 
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'DoB' : 'Date of Birth',
                    'birth_address' : 'Birth Address', 
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'apply_grade_level' : 'Apply Grade Level',
                    'academic_year' : 'Academic Year',
                    'profile_pic' : 'Profile Picture',
                    'health_record' : 'Health Records',
                    'physical_checkup' : 'Physical Checkup',
                    'vaccinated' : 'Vaccinated',
                    'dose_vaccination' : 'Dose of Vaccine',
                    'id_vaccine_card' : 'ID Card of Vaccination',
                    'early_school' : 'Early School',
                    
                    'parent_name' : 'Parent Name', 
                    'parent_occupation' : 'Parent Occupation/Job', 
                    'parent_email' : 'Parent Email', 
                    'parent_contact' : 'Parent Phone Contact',
                    'emergency_cont_name' : 'Contact Name of Emergency',
                    'emergency_contact' : 'Emergency Contact Number',
                    'emergency_address' : 'Emergency Contact Address',
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident',
                    'profile_pic' : 'Profile Picture', 
                }        
class updateprospectform(forms.ModelForm):
    
    class Meta:
        model   = Prospect
        fields  = ['first_name', 'last_name', 'gender', 'DoB', 'birth_address','nationality', 'religion', 'apply_grade_level', 'academic_year', 'profile_pic',
                   'health_record', 'physical_checkup', 'vaccinated', 'dose_vaccination', 'id_vaccine_card', 'early_school', 
                   'parent_name', 'parent_occupation', 'parent_email', 'parent_contact', 'emergency_cont_name', 'emergency_contact', 'emergency_address', 
                   'address', 'city', 'country']
        labels  = { 
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'DoB' : 'Date of Birth',
                    'birth_address' : 'Birth Address', 
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'apply_grade_level' : 'Apply Grade Level',
                    'academic_year' : 'Academic Year',
                    'profile_pic' : 'Profile Picture',
                    'health_record' : 'Health Records',
                    'physical_checkup' : 'Physical Checkup',
                    'vaccinated' : 'Vaccinated',
                    'dose_vaccination' : 'Dose of Vaccine',
                    'id_vaccine_card' : 'ID Card of Vaccination',
                    'early_school' : 'Early School',
                    
                    'parent_name' : 'Parent Name', 
                    'parent_occupation' : 'Parent Occupation/Job', 
                    'parent_email' : 'Parent Email', 
                    'parent_contact' : 'Parent Phone Contact',
                    'emergency_cont_name' : 'Emergency Contact Name',
                    'emergency_contact' : 'Emergency Contact Number',
                    'emergency_address' : 'Emergency Contact Address',
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident',
                    'profile_pic' : 'Profile Picture', 
                }

class Entrance_Examform(forms.ModelForm):
    class Meta:
        model = Entrance_Exam
        fields = ['class_name', 'class_building', 'time_schedule', 'date_exam']
        labels = { 
                    'class_name' : 'Class Name', 
                    'class_building' : 'Class Building', 
                    'time_schedule' : 'Time Schedule',
                    'date_exam' : 'Exam Date', 
                }        
class updateentrance_examform(forms.ModelForm):
    
    class Meta:
        model  = Entrance_Exam
        fields = ['class_name', 'class_building', 'time_schedule', 'date_exam']
        labels = { 
                    'class_name' : 'Class Name', 
                    'class_building' : 'Class Building', 
                    'time_schedule' : 'Exam Schedule', 
                    'date_exam' : 'Exam Date', 
                }

class Enroll_Examform(forms.ModelForm): 
    class Meta:
        model  = Enroll_Exam
        fields = ['prospect_name', 'classroom', 'username']
        labels = { 
                    'prospect_name' : 'Prospect Name', 
                    'classroom' : 'Classroom', 
                    'username' : 'Username', 
                }                             
class updateenroll_examform(forms.ModelForm):
    
    class Meta:
        model  = Enroll_Exam
        fields = ['prospect_name', 'classroom', 'username']
        labels = { 
                    'prospect_name' : 'Prospect Name', 
                    'classroom' : 'Classroom', 
                    'username' : 'Username', 
                }

class Exam_Statsform(forms.ModelForm): 
    class Meta:
        model  = Exam_Stats
        fields = ['exam_card', 'exam_type', 'exam_status', 'exam_score']
        labels = { 
                    'exam_card' : 'Exam ID', 
                    'exam_type' : 'Exam Type', 
                    'exam_status' : 'Exam Status', 
                    'exam_score' : 'Exam Score',
                }
class updateexam_statsform(forms.ModelForm): 
    class Meta:
        model  = Exam_Stats
        fields = ['exam_card', 'exam_type', 'exam_status', 'exam_score']
        labels = { 
                    'exam_card' : 'Exam ID', 
                    'exam_type' : 'Exam Type', 
                    'exam_status' : 'Exam Status', 
                    'exam_score' : 'Exam Score',
                }

class Teacherform(forms.ModelForm):
   
    class Meta:
        model  = Teacher
        fields = ['staff_user', 'first_name', 'last_name', 'gender', 'DoB', 'nationality', 'religion', 'profile_pic', 'bachelor_degree',
                   'email', 'phone_num', 'address', 'city', 'country']
        labels = { 
                    'staff_user' : 'Staff ID',
                    'first_name' : 'First Name',
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender',
                    'DoB' : 'Date of Birth',
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'profile_pic' : 'Profile Picture',
                    'bachelor_degree' : 'Degree Status',
                    
                    'email' : 'Email', 
                    'phone_num' : 'Phone Contact', 
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident', 
                }        
class updateteacherform(forms.ModelForm):
    class Meta:
        model  = Teacher
        fields = ['staff_user', 'first_name', 'last_name', 'gender', 'DoB', 'nationality', 'religion', 'profile_pic', 'bachelor_degree',
                   'email', 'phone_num', 'address', 'city', 'country']
        labels = { 
                    'staff_user' : 'Staff ID',
                    'first_name' : 'First Name',
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender',
                    'DoB' : 'Date of Birth',
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'profile_pic' : 'Profile Picture',
                    'bachelor_degree' : 'Degree Status',
                    
                    'email' : 'Email', 
                    'phone_num' : 'Phone Contact', 
                    
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident', 
                }
        
class Studentform(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['user', 'first_name', 'last_name', 'gender', 'grade_level', 'student_status', 'age', 'DoB', 'nationality', 'religion', 'student_idcard', 'email', 'profile_pic',
                   'father_status', 'father_firstname', 'father_lastname', 'father_occupation', 'mother_status', 'mother_firstname', 'mother_lastname', 'mother_occupation',
                   'parent_email', 'parent_contact1', 'parent_contact2', 'address', 'city', 'country']
        labels = {
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'grade_level' : 'Grade Level',
                    'student_status' : 'Student Status',
                    'age' : 'Age', 
                    'DoB' : 'Date of Birth',
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'student_idcard' : 'Student ID Card',
                    'email' : 'Email',
                    'profile_pic' : 'Profile Picture',
                    
                    'father_status' : 'Living Status', 
                    'father_firstname' : 'Father First Name',
                    'father_lastname' : 'Father Last Name',
                    'father_occupation' : 'Father Occupation/Job', 
                    'mother_status' : 'Living Status',
                    'mother_firstname' : 'Mother First Name', 
                    'mother_lastname' : 'Mother Last Name', 
                    'mother_occupation' : 'Mother Occupation/Job', 
                    
                    'parent_email' : 'Parent Email',
                    'parent_contact1' : 'Parent Contact #1',
                    'parent_contact2' : 'Parent Contact #2',
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident', 
                }        
class updatestudentform(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['user', 'first_name', 'last_name', 'gender', 'grade_level', 'student_status', 'age', 'DoB', 'nationality', 'religion', 'student_idcard', 'email', 'profile_pic',
                   'father_status', 'father_firstname', 'father_lastname', 'father_occupation', 'mother_status', 'mother_firstname', 'mother_lastname', 'mother_occupation',
                   'parent_email', 'parent_contact1', 'parent_contact2', 'address', 'city', 'country']
        labelsb= { 
                    'first_name' : 'First Name', 
                    'last_name' : 'Last Name', 
                    'gender' : 'Gender', 
                    'grade_level' : 'Grade Level',
                    'student_status' : 'Student Status',
                    'age' : 'Age', 
                    'DoB' : 'Date of Birth', 
                    'nationality' : 'Nationality',
                    'religion' : 'Religion',
                    'student_idcard' : 'student_idcard',
                    'email' : 'Email',
                    'profile_pic' : 'Profile Picture',
                    
                    'father_status' : 'Living Status',
                    'father_firstname' : 'Father First Name',
                    'father_lastname' : 'Father Last Name', 
                    'father_occupation' : 'Father Occupation/Job', 
                    'mother_status' : 'Living Status',
                    'mother_firstname' : 'Mother First Name', 
                    'mother_lastname' : 'Mother Last Name', 
                    'mother_occupation' : 'Mother Occupation/Job', 
                    
                    'parent_email' : 'Parent Email',
                    'parent_contact1' : 'Parent Contact #1',
                    'parent_contact2' : 'Parent Contact #2',
                    'address' : 'Address',
                    'city' : 'City',
                    'country' : 'Country of Resident', 
                }
       
class Staffform(forms.ModelForm):
   
    class Meta:
        model = Staff
        fields = ['user', 'card_number','first_name', 'last_name', 'gender', 'contact', 'status', 'profile_pic', 'position']
        labels = {
                    'user' : 'User',
                    'card_number': 'Employee ID',
                    'first_name' : 'First Name',
                    'last_name' : 'Last Name',
                    'gender' : 'Gender',
                    'contact' : 'Contact',
                    'position' : 'Position', 
                    'profile_pic' : 'Profile Picture',
                    'status' : 'Status', 
            }
class updatestaffform(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ['card_number','first_name', 'last_name', 'gender', 'contact', 'position', 'profile_pic', 'status']
        labels = {
                    'card_number':'Employee ID',
                    'first_name' : 'First Name',
                    'last_name' : 'Last Name',
                    'gender' : 'Gender',
                    'contact' : 'Contact',
                    'position' : 'Position',
                    'profile_pic' : 'Profile Picture',
                    'status' : 'Status',
            }

class Staff_Userform(forms.ModelForm):
   
    class Meta:
        model = Staff_User
        fields = ['username','card_number', 'profile_pic']
        labels = {
                    'username': 'Username',
                    'card_number' : 'Card Number',
                    'profile_pic' : 'Profile Picture',
            }
class updatestaff_userform(forms.ModelForm):
    
    class Meta:
        model = Staff_User
        fields = ['username','card_number', 'profile_pic']
        labels = {
                    'username':'Username',
                    'card_number' : 'Card Number',
                    'profile_pic' : 'Profile Picture',
            }
                
class Subjectform(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = ['grade_level', 'class_subject']
        labels = { 
                    'grade_level' : 'Grade Level', 
                    'class_subject' : 'Class Subject',
                }        
class updatesubjectform(forms.ModelForm):
        
    class Meta:
        model = Subject
        fields = ['grade_level', 'class_subject']
        labels = { 
                    'grade_level' : 'Grade Level', 
                    'class_subject' : 'Class Subject',
                }
        
class Classroomform(forms.ModelForm):
    
    class Meta:
        model = Classroom
        fields = ['class_level', 'homeroom_teacher', 'subject', 'class_bld', 'class_capacity']
        labels = {
                    'class_level' : 'Grade Level', 
                    'homeroom_teacher' : 'Homeroom Teacher', 
                    'subject' : 'Class Subject', 
                    'class_bld' : 'Class Building', 
                    'class_capacity' : 'Class Capacity', 
                }       
class updateclassroomform(forms.ModelForm):
    
    class Meta:
        model = Classroom
        fields = ['class_level', 'homeroom_teacher', 'subject', 'class_bld', 'class_capacity']
        labels = {
                    'class_level' : 'Grade Level', 
                    'homeroom_teacher' : 'Homeroom Teacher', 
                    'subject' : 'Class Subject', 
                    'class_bld' : 'Class Building', 
                    'class_capacity' : 'Class Capacity', 
                }
  
class Enroll_NStudentform(forms.ModelForm):
   
    class Meta:
        model = Enroll_NStudent
        fields = ['student_user', 'examid_card', 'into_class', 'academic_year']
        labels = { 
                    'student_user' : 'Student User',
                    'examid_card' : 'Examinee Card',  
                    'into_class' : 'Enroll into Class', 
                    'academic_year' : 'Academic Year', 
                }        
class updateenroll_nstudentform(forms.ModelForm):
   
    class Meta:
        model = Enroll_NStudent
        fields = ['student_user', 'examid_card', 'into_class', 'academic_year']
        labels = { 
                    'student_user' : 'Student User',
                    'examid_card' : 'Examinee Card', 
                    'into_class' : 'Enroll into Class', 
                    'academic_year' : 'Academic Year', 
                }

class Class_Academicform(forms.ModelForm):
   
    class Meta:
        model = Class_Academic
        fields = ['class_academic', 'student_class']
        labels = {  
                    'class_academic' : 'Class Academic Year',
                    'student_class' : 'Student Class',
                }             
class updateclass_academicform(forms.ModelForm):
   
    class Meta:
        model = Class_Academic
        fields = ['class_academic', 'student_class']
        labels = {  
                    'class_academic' : 'Class Academic Year',
                    'student_class' : 'Student Class',
                }
        
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "country",
            "state",
            "city",
            "street",
        )
  # State
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:
            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'name')

    # City
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state:
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')

    # Street
        self.fields['street'].queryset = State.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['street'].queryset = Street.objects.filter(
                    city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.city:
            self.fields['street'].queryset = self.instance.city.street_set.order_by(
                'name')