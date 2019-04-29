from django.db import models


# Create your models here.
class Instructors(models.Model):
    class Meta:
        db_table = "Instructors"
    
    Instructor_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    def __str__(self):
        return self.Name


class Courses(models.Model):
    class Meta:
        db_table = "Courses"
    
    Course_id = models.CharField(max_length=10,primary_key = True)
    Course_Name = models.CharField(max_length=200)
    Course_credits = models.IntegerField()
    Lectures = models.IntegerField()
    Lab = models.IntegerField()
    Practicals = models.IntegerField()
    #BATCH
    Semester = models.IntegerField()
    Course_Type = models.BooleanField(help_text="Tick if this is an Elective",verbose_name="Elective")
    Instructor_id = models.ForeignKey(Instructors,on_delete= models.CASCADE)
    def __str__(self):
        return self.Course_Name

    def getInstructor(self):
        return self.Instructor_id


class Students(models.Model):
    class Meta:
        db_table = "Students"
    
    Student_id = models.CharField(primary_key=True, max_length=200)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Batch = models.CharField(max_length=10)
    Branch = models.CharField(max_length=10,default = 'nill')
    CGPA = models.DecimalField(default = 0.00,max_digits=4,decimal_places=2)
    Semester = models.IntegerField(default=1)
    courses = models.ManyToManyField(Courses)
    
    def __str__(self):
        return self.Name
    def Stu_id(self):
        return self.Student_id





class Grades(models.Model):#GRADES
    class Meta:
        db_table = "Grades"

    Student_id = models.ForeignKey(Students,on_delete = models.CASCADE)
    Course_id = models.ForeignKey(Courses,on_delete = models.CASCADE)
    Grade = models.CharField(max_length=2)
    #if(Students.)

class Document(models.Model):
    instructor_id = models.CharField(max_length=255, blank=True)
    course_id = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')

class StudentsDocument(models.Model):
    #Student_id = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')

class CoursesDocument(models.Model):
    document = models.FileField(upload_to='documents/')

# class GG(models.Model):
#     Student_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     Course_id= models.ForeignKey(Students, on_delete=models.CASCADE)
#     Grade = models.CharField(max_length=2)
#     class Meta:
#         unique_together = ['Student_id', 'Course_id']