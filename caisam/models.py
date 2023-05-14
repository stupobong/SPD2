from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model
from datetime import date


# Create your models here.
# ------------------------------------------------------------------------------ Registree Entrance Exam Database --------------------------------------------------------------------------------
#Academic Year Model
class Academic_Year(models.Model):
    
    SCHOOL_YEAR = (
                ('2021-2022', '2021-2022'),
                ('2022-2023', '2022-2023'),
                ('2023-2024', '2023-2024'),
                ('2024-2025', '2024-2025'),
            )
    
    academic_year          = models.CharField(max_length=100, null=True, default="2023-2024", choices=SCHOOL_YEAR)
    start_end_year         = models.CharField(max_length=100, unique=False, null=True, default="Academic Year of August 2023 - May 2024")
    date_added             = models.DateField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
            return self.start_end_year
  

#Application Model   
class Registree(models.Model):
    GENDER = (
                ('Female', 'Female'),
                ('Male', 'Male'),
            )
    STATUS = (
                ('Transfer', 'Transfer'),
                ('New', 'New'),
                ('Existing', 'Existing'),
                ('Inactive', 'Inactive'),
            )
    RELIGION = (
                ('SDA Christian', 'SDA Christian'),
                ('Christian', 'Christian'),
                ('Muslim', 'Muslim'),
                ('Buddhism', 'Buddhism'),
            )
    SCHOOL_YEAR = (
                ('2021-2022', '2021-2022'),
                ('2022-2023', '2022-2023'),
                ('2023-2024', '2023-2024'),
                ('2024-2025', '2024-2025'),
            )
    NATIONALITY = (
                    ('Cambodian', 'Cambodian'),
                    ('Thai', 'Thai'),
                    ('Asian', 'Asian'),
                    ('Others', 'Others'),
                    )
    COUNTRY = (
                    ('Cambodia', 'Cambodia'),
                    ('Thailand', 'Thailand'),
                    ('Asia', 'Asia'),
                    ('Others', 'Others'),
                    )
    GRADE_LEVEL = (
                ('Grade 12', 'Grade 12'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Grade 9', 'Grade 9'),
                ('Grade 8', 'Grade 8'), ('Grade 7', 'Grade 7'), ('Grade 6', 'Grade 6'), ('Grade 5', 'Grade 5'), ('Grade 4', 'Grade 4'),
                ('Grade 3', 'Grade 3'), ('Grade 2', 'Grade 2'), ('Grade 1', 'Grade 1'), ('Grade K', 'Grade K'),
            )
    
    #Registree Information   
    first_name           = models.CharField(max_length=100, unique=False, null=False)
    last_name            = models.CharField(max_length=100, unique=False, null=False)
    gender               = models.CharField(max_length=100, null=True, choices=GENDER)
    DoB                  = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='date of birth')
    nationality          = models.CharField(max_length=100, null=True, default="Cambodian", choices=NATIONALITY)
    religion             = models.CharField(max_length=100, null=True, default="SDA Christian", choices=RELIGION)
    grade_level          = models.CharField(max_length=100, null=True, default="Grade 8", choices=GRADE_LEVEL)
    academic_year        = models.CharField(max_length=100, null=True, default="2022-2023", choices=SCHOOL_YEAR)
    profile_pic          = models.ImageField(null=True, blank=True)
    
    #Applicant-Parent Contact Information
    parent_name          = models.CharField(max_length=60, unique=False, null=True)
    parent_occupation    = models.CharField(max_length=60, unique=False, null=True)
    parent_email         = models.CharField(max_length=60, unique=False, null=True)
    parent_contact       = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    
    #Applicant Information
    address              = models.CharField(max_length=60, unique=False, null=True)
    city                 = models.CharField(max_length=60, unique=False, null=True)
    country              = models.CharField(max_length=60, unique=False, null=True)
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return str(self.first_name) + ' '+ self.last_name 

#Prospect New Student Registration Model   
class Prospect(models.Model):
    GENDER = (
                ('Female', 'Female'),
                ('Male', 'Male'),
            )
    STATUS = (
                ('Transfer', 'Transfer'),
                ('New', 'New'),
                ('Existing', 'Existing'),
                ('Inactive', 'Inactive'),
            )
    RELIGION = (
                ('SDA Christian', 'SDA Christian'),
                ('Christian', 'Christian'),
                ('Muslim', 'Muslim'),
                ('Buddhism', 'Buddhism'),
            )
    SCHOOL_YEAR = (
                ('2021-2022', '2021-2022'),
                ('2022-2023', '2022-2023'),
                ('2023-2024', '2023-2024'),
                ('2024-2025', '2024-2025'),
            )
    NATIONALITY = (
                    ('Cambodian', 'Cambodian'),
                    ('Thai', 'Thai'),
                    ('Asian', 'Asian'),
                    ('Others', 'Others'),
                    )
    COUNTRY = (
                    ('Cambodia', 'Cambodia'),
                    ('Thailand', 'Thailand'),
                    ('Asia', 'Asia'),
                    ('Others', 'Others'),
                    )
    GRADE_LEVEL = (
                ('Grade 12', 'Grade 12'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Grade 9', 'Grade 9'),
                ('Grade 8', 'Grade 8'), ('Grade 7', 'Grade 7'), ('Grade 6', 'Grade 6'), ('Grade 5', 'Grade 5'), ('Grade 4', 'Grade 4'),
                ('Grade 3', 'Grade 3'), ('Grade 2', 'Grade 2'), ('Grade 1', 'Grade 1'), ('Grade K', 'Grade K'),
            )
    ALLERGIC = (
                    ('Heart problems', 'Heart problems'),
                    ('High Blood Pressure', 'High Blood Pressure'),
                    ('ADHD', 'ADHD'),
                    ('Eating Disorder', 'Eating Disorder'),
                    ('Medicine', 'Medicine'),
                    ('Food Allergic', 'Food Allergic'),
                    ('Injury', 'Injury'),
                    ('Mental Health', 'Mental Health'),
                    ('None', 'None'),
                    ('Others', 'Others'),
                    )
    PHYSICAL_CHECKUP = (
                ('Yes', 'Yes'),
                ('No', 'No'),
            )
    VACCINATED = (
                ('Yes', 'Yes'),
                ('No', 'No'),
            )
    DOSE_VACCINATION = (
                ('1st Dose', '1st Dose'),
                ('2nd Dose', '2nd Dose'),
                ('3rd Dose', '3rd Dose'),
                ('4th Dose', '4th Dose'),
                ('5th Dose', '5h Dose'),
                ('6th Dose', '6th Dose'),
            )
    
    #Prospect Information   
    first_name           = models.CharField(max_length=100, unique=False, null=False)
    last_name            = models.CharField(max_length=100, unique=False, null=False)
    gender               = models.CharField(max_length=100, null=True, choices=GENDER)
    DoB                  = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='date of birth')
    birth_address        = models.CharField(max_length=60, unique=False, null=True)
    nationality          = models.CharField(max_length=100, null=True, default="Cambodian", choices=NATIONALITY)
    religion             = models.CharField(max_length=100, null=True, default="--Select--", choices=RELIGION)
    apply_grade_level    = models.CharField(max_length=100, null=True, default="--Select--", choices=GRADE_LEVEL)
    academic_year        = models.CharField(max_length=100, null=True, default="2022-2023", choices=SCHOOL_YEAR)
    profile_pic          = models.ImageField(null=True, blank=True)

    
    #Health Records Information    
    health_record        = models.CharField(max_length=100, null=True, default="None", choices=ALLERGIC)    
    physical_checkup     = models.CharField(max_length=100, null=True, default="Yes", choices=PHYSICAL_CHECKUP)    
    vaccinated           = models.CharField(max_length=100, null=True, default="Yes", choices=VACCINATED)    
    dose_vaccination     = models.CharField(max_length=100, null=True, default="Yes", choices=DOSE_VACCINATION)    
    id_vaccine_card      = models.CharField(max_length=60, unique=False, null=True)
    early_school         = models.CharField(max_length=100, null=True, default="School Name")
    
    #Applicant-Parent Contact Information
    parent_name          = models.CharField(max_length=60, unique=False, null=True)
    parent_occupation    = models.CharField(max_length=60, unique=False, null=True)
    parent_email         = models.CharField(max_length=60, unique=False, null=True)
    parent_contact       = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    emergency_cont_name  = models.CharField(max_length=60, unique=False, null=True)
    emergency_contact    = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    emergency_address    = models.CharField(max_length=60, unique=False, null=True)
    
    #Applicant Information
    address              = models.CharField(max_length=60, unique=False, null=True)
    city                 = models.CharField(max_length=60, unique=False, null=True)
    country              = models.CharField(max_length=60, unique=False, null=True)
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return str(self.first_name) + ' '+ self.last_name 

#Class_Entrance Model
class Entrance_Exam (models.Model):
    
    BUILDING = (
                ('Main Bld.', 'Main Bld.'),
                ('Library Bld.', 'Library Bld.'),
                ('Picnic', 'Picinic'),
                ('12th Grade Bld.', '12th Grade Bld.'),
    )
    
    GRADE_LEVEL = (
                ('Grade K-3', 'Grade K-3'),
                ('Grade 4-8', 'Grade 4-8'),
                ('Grade 9-12', 'Grade 9-12'),
            )
    
    TIME_SCHEDULE = (
                ('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
    )
    
    DATE_EXAM = (
                ('12th of June', '12th of June'),
                ('13th of June', '13th of June'),
                ('14th of June', '14th of June'),
                ('15th of June', '15th of June'),
    )
    
    class_name           = models.CharField(max_length=100, null=True, default="Grade k-3", choices=GRADE_LEVEL)
    class_building       = models.CharField(max_length=100, null=True, default="Main Bld.", choices=BUILDING)
    time_schedule        = models.CharField(max_length=100, null=True, default="Morning", choices=TIME_SCHEDULE)
    date_exam            = models.CharField(max_length=100, null=True, default="13th of June", choices=DATE_EXAM)  
    
    def __str__(self):
        return str(self.class_name) + ' '+ self.time_schedule+ ' '+self.date_exam

#Enroll Exam Model
class Enroll_Exam(models.Model):
    
    prospect_name        = models.ForeignKey(Prospect, on_delete= models.CASCADE, default="202200220", related_name="prospect_id_fk")
    classroom            = models.ForeignKey(Entrance_Exam, on_delete= models.CASCADE, related_name="entrance_exam_id_fk")
    username             = models.CharField(max_length=60, unique=False, null=True)
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
        return self.username
       
#Exam Model
class Exam_Stats(models.Model):
    EXAM_STATUS = (
                ('PASS', 'PASS'),
                ('FAIL', 'FAIL'),
    )
    
    EXAM_TYPE = (
                ('IELTS', 'IELTS'),
                ('WIDA', 'WIDA'),
                ('MAP TEST', 'MAP TEST'),
    )
    
    exam_card            = models.OneToOneField(Enroll_Exam, null=True, on_delete=models.CASCADE)
    exam_type            = models.CharField(max_length=100, null=True, default="WIDA", choices=EXAM_TYPE)
    exam_status          = models.CharField(max_length=100, null=True, default="PASS", choices=EXAM_STATUS)
    exam_score           = models.CharField(max_length=100, unique=False, default="%", null=False)
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
            return self.exam_card.username
    
           
# ------------------------------------------------------------------------------ School Teacher Database --------------------------------------------------------------------------------

class Staff(models.Model):
    GENDER = (
                ('Female', 'Female'),
                ('Male', 'Male')
            )
    STATUS = (
                ('Active', 'Active'),
                ('Inactive', 'Inactive')
            )
    
    POSITION = (
                ('Principal', 'Principal'),
                ('Vice-Principal', 'Vice-Principal'),
                ('HR', 'HR'),
                ('Janitor', 'Janitor'),
                ('Guard', 'Guard'),
                ('Maintenance', 'Maintenance'),
                ('Homeroom Teacher', 'Homeroom Teacher'),
                ('Subject Teacher', 'Subject Teacher'),
                ('Teacher Assistant', 'Teacher Assistant'),
                ('Librarian', 'Librarian'),
                ('Registrar', 'Registrar'),
                ('Accountant', 'Accountant'),      
            ) 
    user                 = models.OneToOneField(User, null=True, on_delete=models.CASCADE)            
    card_number          = models.CharField(max_length=60, unique=True, null=True)
    first_name           = models.CharField(max_length=100, unique=False, null=False)
    last_name            = models.CharField(max_length=100, unique=False, null=False)
    gender               = models.CharField(max_length=100, null=True, choices=GENDER)
    contact              = models.CharField(max_length=60, unique=False, default="+855 ", null=True)
    position             = models.CharField(max_length=200, null=False, choices=POSITION)
    status               = models.CharField(max_length=100, null=True, default="Active", choices=STATUS)
    profile_pic          = models.ImageField(null=True, blank=True)
    date_added           = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
        return str(self.card_number)+ ' '+ self.first_name

class Staff_User(models.Model):
    
    username             = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    card_number          = models.ForeignKey(Staff, on_delete= models.CASCADE, related_name="staffs_id_fk")
    profile_pic          = models.ImageField(null=True, blank=True)
    date_added           = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
            return self.card_number.card_number
        
        
class Teacher(models.Model):
    GENDER = (
                ('Female', 'Female'),
                ('Male', 'Male')
            )
    RELIGION = (
                ('SDA Christian', 'SDA Christian'),
                ('Christian', 'Christian'),
                ('Muslim', 'Muslim'),
                ('Buddhism', 'Buddhism'),
            )
    NATIONALITY = (
                    ('Thai', 'Thai'),
                    ('Asian', 'Asian'),
                    ('Others', 'Others'),
                    ('Cambodian', 'Cambodian'),
                    ('Phillipines', 'Phillipines'),
                    )
    COUNTRY = (
                ('Cambodia', 'Cambodia'),
                ('Others', 'Others'),
            )
    BACHELOR_DEGREE = (
                ('BS of IT', 'BS of IT'),
                ('BA of TESOL', 'BA of TESOL'),
                ('BS of Science', 'BS of Science'),
                ('BA of Theology', 'BA of Theology'),
                ('MBA of Theology', 'MBA of Theology'),
                ('BA of Education', 'BA of Education'),
                ('MBA of Education', 'MBA of Education'),
                ('MBA of Administration', 'MBA of Administration'),
            )
    
    #Teacher Basic Information 
    staff_user           = models.OneToOneField(Staff, null=True, on_delete=models.CASCADE)
    first_name           = models.CharField(max_length=60, unique=False, null=True)
    last_name            = models.CharField(max_length=60, unique=False, null=True)
    gender               = models.CharField(max_length=100, null=True, choices=GENDER)
    DoB                  = models.DateField(auto_now=False, null=True, auto_now_add=False, verbose_name='date of birth')
    nationality          = models.CharField(max_length=100, null=True, default="Cambodian", choices=NATIONALITY)
    religion             = models.CharField(max_length=100, null=True, default="SDA Christian", choices=RELIGION)
    
    #Teacher Personal Qualification
    profile_pic          = models.ImageField(null=True, blank=True)
    bachelor_degree      = models.CharField(max_length=100, null=True, default="BA of Science", choices=BACHELOR_DEGREE)
    
    #Teacher Contact Information
    email                = models.CharField(max_length=60, unique=False, default=" @caisedu.com", null=True)
    phone_num            = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    address              = models.CharField(max_length=60, unique=False, null=True)
    city                 = models.CharField(max_length=60, unique=False, null=True)
    country              = models.CharField(max_length=100, null=True, default="Cambodia", choices=COUNTRY)
    date_joined          = models.DateField(verbose_name='date joined', auto_now_add=False, auto_now=False, null=True)
    
    def __str__(self):
        return str(self.first_name) + ' '+ self.last_name

# ------------------------------------------------------------------------------ School Enrollment Class Database --------------------------------------------------------------------------------
#Subjects Attributes Model
class Subject(models.Model):
    
    GRADE_LEVEL = (
                ('Grade 12A', 'Grade 12A'), ('Grade 12B', 'Grade 12B'), ('Grade 11A', 'Grade 11A'), ('Grade 11B', 'Grade 11B'), ('Grade 10A', 'Grade 10A'), ('Grade 10B', 'Grade 10B'), ('Grade 9A', 'Grade 9A'), ('Grade 9B', 'Grade 9B'),
                ('Grade 8A', 'Grade 8A'), ('Grade 8B', 'Grade 8B'), ('Grade 7A', 'Grade 7A'), ('Grade 7B', 'Grade 7B'),('Grade 6A', 'Grade 6A'), ('Grade 6B', 'Grade 6B'), ('Grade 5A', 'Grade 5A'), ('Grade 5B', 'Grade 5B'), ('Grade 4A', 'Grade 4A'), ('Grade 4B', 'Grade 4B'),
                ('Grade 3A', 'Grade 3A'), ('Grade 3B', 'Grade 3B'), ('Grade 2A', 'Grade 2A'), ('Grade 2B', 'Grade 2B'), ('Grade 1A', 'Grade 1A'), ('Grade 1B', 'Grade 1B'), ('Grade KA', 'Grade KA'), ('Grade KB', 'Grade KB'),
            )
    
    CLASS_SUBJECT = (
                ('A', 'Computer'), ('B', 'Computer Literacy'), ('C', 'Computer Keyboarding'), ('D', 'Yearbook'), ('E', 'Art Appreciation'), 
                ('F', 'Music'), ('G', 'Music Appreciation'), ('H', 'Arts'), ('I', 'Art Appreciation'), ('J', 'P.E.'), ('K', 'Drama'), ('L', 'Library'), 
                ('M', 'Science'), ('N', 'Homelife'), ('O', 'Physical Science'), ('P', 'Biology'),  ('Q', 'Physic'), ('R', 'Chemistry'), 
                ('S', 'Mathematic'), ('T', 'Pre-Algebra'), ('U', 'Algebra I'), ('V', 'Algebra II'), ('W', 'Pre-Calculus'), 
                ('X', 'Social Studies'), ('Y', 'World History'), ('Z', 'Ancient History'), ('AA', 'Morality'), ('AB', 'Pathfinder'), ('AC', 'Chapel'), 
                ('AD', 'Khmer'), ('AE', 'Khmer Geography'), ('AF', 'Khmer Literacy'), 
                ('AG', 'Reading/Handwriting'),('AH', 'English/Spelling'), ('AI', 'English I'), ('AJ', 'English II'), ('AK', 'English IIII'), 
                 
            )
        
    grade_level           = models.CharField(max_length=100, null=True, default="Grade 7", choices=GRADE_LEVEL)
    class_subject         = MultiSelectField (max_length=300, max_choices=15, null=True, default="A", choices=CLASS_SUBJECT)
    date_added            = models.DateField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
            return self.grade_level

#Classroom Attributes Model
class Classroom(models.Model):
    CAPACITY = (
                ('25', '25'),
                ('30', '30'),
                ('20', '20'),
    )
    
    CLASS_BLD = (
                ('Main Bld.', 'Main Bld.'),
                ('Library Bld.', 'Library Bld.'),
                ('Picnic', 'Picinic'),
                ('12th Grade Bld.', '12th Grade Bld.'),
    )
    
    CLASS_LEVEL = (
                ('Grade 12A', 'Grade 12A'), ('Grade 12B', 'Grade 12B'), ('Grade 11A', 'Grade 11A'), ('Grade 11B', 'Grade 11B'), ('Grade 10A', 'Grade 10A'), ('Grade 10B', 'Grade 10B'), ('Grade 9A', 'Grade 9A'), ('Grade 9B', 'Grade 9B'),
                ('Grade 8A', 'Grade 8A'), ('Grade 8B', 'Grade 8B'), ('Grade 7A', 'Grade 7A'), ('Grade 7B', 'Grade 7B'),('Grade 6A', 'Grade 6A'), ('Grade 6B', 'Grade 6B'), ('Grade 5A', 'Grade 5A'), ('Grade 5B', 'Grade 5B'), ('Grade 4A', 'Grade 4A'), ('Grade 4B', 'Grade 4B'),
                ('Grade 3A', 'Grade 3A'), ('Grade 3B', 'Grade 3B'), ('Grade 2A', 'Grade 2A'), ('Grade 2B', 'Grade 2B'), ('Grade 1A', 'Grade 1A'), ('Grade 1B', 'Grade 1B'), ('Grade KA', 'Grade KA'), ('Grade KB', 'Grade KB'),
            )
    class_level           = models.CharField(max_length=100, null=True, default="Grade 12A", choices=CLASS_LEVEL)
    homeroom_teacher      = models.ForeignKey(Teacher, on_delete= models.CASCADE, related_name="hr_teacher_id_fk")
    subject               = models.ForeignKey(Subject, on_delete= models.CASCADE, related_name="subject_id_fk")
    class_bld             = models.CharField(max_length=100, null=True, default="Main Bld.", choices=CLASS_BLD)
    class_capacity        = models.CharField(max_length=100, null=True, default="25", choices=CAPACITY)
    date_added            = models.DateField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
            return self.class_level
       
#NStudent Enrollment Model
class Enroll_NStudent(models.Model):
    STUDENT_STATUS = (
                ('New Student', 'New Student'),
                ('Existing Student', 'Existing Student'),
            )
    
    APPROVE_STATUS = (
                ('Enrollment Approved', 'Enrollment Approved'),
                ('Enrollment Rejected', 'Enrollment Rejected'),
                ('IN PROBATION', 'IN PROBATION'),
            )
    
    student_user         = models.OneToOneField(User, null=True, on_delete=models.CASCADE)    
    examid_card          = models.ForeignKey(Exam_Stats, on_delete= models.CASCADE, related_name="exam_id_fk")
    into_class           = models.ForeignKey(Classroom, on_delete= models.CASCADE, related_name="class_level_id_fk")
    academic_year        = models.ForeignKey(Academic_Year, on_delete= models.CASCADE, related_name="academic_year_id_fk")
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)

    class Meta:
        verbose_name_plural = "New Student Enrollment"

    def __str__(self):
            return self.into_class.class_level

#Student Model 
class Student(models.Model):
    
    GENDER = (
                ('Female', 'Female'),
                ('Male', 'Male'),
            )
    STUDENT_STATUS = (
                ('New Student', 'New Student'),
                ('Existing Student', 'Exisiting Student'),
            )
    PARENT_STATUS = (
                ('Living', 'Living'),
                ('Deceased', 'Deceased'),
            )
    RELIGION = (
                ('SDA Christian', 'SDA Christian'),
                ('Christian', 'Christian'),
                ('Muslim', 'Muslim'),
                ('Buddhism', 'Buddhism'),
            )
    NATIONALITY = (
                    ('Thai', 'Thai'),
                    ('Asian', 'Asian'),
                    ('Others', 'Others'),
                    ('Cambodian', 'Cambodian'),
                    ('Phillipines', 'Phillipines'),
                    )
    COUNTRY_ADDRESS = (
                ('Cambodia', 'Cambodia'),
                ('Others', 'Others'),
            )
    GRADE_LEVEL = (
                ('Grade 12', 'Grade 12'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Grade 9', 'Grade 9'),
                ('Grade 8', 'Grade 8'), ('Grade 7', 'Grade 7'), ('Grade 6', 'Grade 6'), ('Grade 5', 'Grade 5'), ('Grade 4', 'Grade 4'),
                ('Grade 3', 'Grade 3'), ('Grade 2', 'Grade 2'), ('Grade 1', 'Grade 1'), ('Grade K', 'Grade K'),
            )
    
    #Student Basic Information
     
    user                 = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  
    first_name           = models.CharField(max_length=100, unique=False, null=False)
    last_name            = models.CharField(max_length=100, unique=False, null=False)
    gender               = models.CharField(max_length=100, null=True, choices=GENDER)
    grade_level          = models.CharField(max_length=100, null=True, default="Grade 5", choices=GRADE_LEVEL)
    student_status       = models.CharField(max_length=100, null=True, default="New Student", choices=STUDENT_STATUS)
    age                  = models.CharField(max_length=100, unique=False, null=False)
    DoB                  = models.DateField(auto_now=False, null=True, default="YYYY-MM-DD", auto_now_add=False, verbose_name='date of birth')
    nationality          = models.CharField(max_length=100, null=True, default="Cambodian", choices=NATIONALITY)
    religion             = models.CharField(max_length=100, null=True, default="SDA Christian", choices=RELIGION)
    student_idcard       = models.CharField(max_length=60, unique=False, default='201600...', null=False)
    email                = models.CharField(max_length=60, unique=False, default=" @caisedu.com", null=True)
    profile_pic          = models.ImageField(null=True, blank=True)
    
    #Student Parental Information
    father_status        = models.CharField(max_length=100, null=True, default="Living", choices=PARENT_STATUS)
    father_firstname     = models.CharField(max_length=60, unique=False, null=True)
    father_lastname      = models.CharField(max_length=60, unique=False, null=True)
    father_occupation    = models.CharField(max_length=60, unique=False, null=True)
    mother_status        = models.CharField(max_length=100, null=True, default="Living", choices=PARENT_STATUS)
    mother_firstname     = models.CharField(max_length=60, unique=False, null=True)
    mother_lastname      = models.CharField(max_length=60, unique=False, null=True)
    mother_occupation    = models.CharField(max_length=60, unique=False, null=True)
    
    
    #Student Contact Information
    parent_email         = models.CharField(max_length=60, unique=False, null=True)
    parent_contact1      = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    parent_contact2      = models.CharField(max_length=60, default="+855 ", unique=False, null=True)
    address              = models.CharField(max_length=60, unique=False, null=True)
    city                 = models.CharField(max_length=60, unique=False, null=True)
    country              = models.CharField(max_length=100, null=True, default="Cambodia", choices=COUNTRY_ADDRESS)
    date_joined          = models.DateField(verbose_name='date joined', auto_now_add=False, auto_now=False, null=True)

    def __str__(self):
        return str(self.last_name) + ' '+ self.first_name 
       
#NStudent Enrollment Model
class Class_Academic(models.Model):
    SCHOOL_YEAR = (
                ('August 2021- June 2022', 'August 2021- June 2022'),
                ('August 2022- June 2023', 'August 2022- June 2023'),
                ('August 2023- June 2024', 'August 2023- June 2024'),
                ('August 2024- June 2025', 'August 2024- June 2025'),
            )
    class_academic       = models.ForeignKey(Classroom, on_delete= models.CASCADE, default="Grade 12", related_name="class_academic_id_fk")
    student_class        = models.ForeignKey(Student, on_delete= models.CASCADE, default="01", related_name="student_id_fk")
    date_added           = models.DateField(verbose_name='date joined', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Class_Academic"

    def __str__(self):
            return self.class_academic.class_level



# Importing excel into database
# #https://labpys.com/import-data-from-excel-into-database-using-django/

class Address(models.Model):
    address = models.CharField(max_length=60, unique=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey('State', blank=True, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True, blank=True)
    street = models.ForeignKey('Street', on_delete=models.SET_NULL, null=True, blank=True)

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class Street(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]