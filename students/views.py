from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import *
#import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render

import pandas as pd



# Create your views here.

def index(request):
    student_entries = Students.objects.all()
    course_entries = Courses.objects.all()
    course_entries = Courses.objects.all()

    instructor_entries = Instructors.objects.all()
    # Grade_entries = Grades.objects.all()
    template = loader.get_template('students/index.html')
    context = {
        'students_entries' : student_entries,
        'courses_entries' : course_entries,
        'instructors_entries' : instructor_entries,
        # 'Grade_entries':Grade_entries,
    }
    return HttpResponse(template.render(context,request))

def student_home(request):
    return render(request,'students/student_home.html')

def admin_home(request):
    return render(request,'students/admin_home.html')
def get_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student_id=form.cleaned_data['your_id']
            student=Students.objects.get(Student_id=student_id)
            Grade_entries = Grades.objects.filter(Student_id=student_id)
            template = loader.get_template('students/list.html')
            context = {
                'students_entries' : student,
                'Grade_entries':Grade_entries,
            }
            return HttpResponse(template.render(context,request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'students/name.html', {'form': form})



def cgpa(request,Student_id):
    
    return HttpResponse("Student %s" % students[1].Email)

def grade(request,Instructor_id):
    instructors = Instructors.objects.all()
    return HttpResponse ("Instructor Name %s" % instructors[0].Name)

# def grade_student(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():

#             form.save()
#             return HttpResponseRedirect('/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'students/grades.html', {'form': form})

def update_gpa(student):
    students=Students.objects.all()
    for student in students:
        grades=Grades.objects.filter(Student_id=student.Student_id)
        total_credits=0
        sum_credit=0
        for grade in grades:
            course=Courses.objects.get(Course_Name=grade.Course_id)
            credit=course.Course_credits
            total_credits+=credit
            sum_credit+=float(grade.Grade)*credit
        student.CGPA=sum_credit/total_credits
        student.save()
    return HttpResponseRedirect('/')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instructor_id=str(form.cleaned_data['instructor_id'])
            course=str(form.cleaned_data['course_id'])
            if(str(Courses.objects.get(Course_id=course).Instructor_id)==str(Instructors.objects.get(Instructor_id=instructor_id).Name)):
                dfs = pd.read_excel('documents/'+str(form.cleaned_data['document']))
                for r in dfs.iterrows():
                    student=Students.objects.get(Student_id=r[1]['Student ID'])
                    course_instance=Courses.objects.get(Course_id=course)
                    # print(student)
                    # print(type(r[1]['Student ID']))
                    grade=Grades.objects.create(Course_id=course_instance,Grade=r[1]['Grade'],Student_id=student)
                    # print(r[1]['Student ID'],"\n\n")    
                return HttpResponseRedirect('/')  
            else:
                return HttpResponse("Permission Denied")
    else:
        form = DocumentForm()
    return render(request, 'students/model_form_upload.html', {
        'form': form
    })


def student_upload(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #student=str(form.cleaned_data['Student_id'])
            dfs = pd.read_excel('documents/'+str(form.cleaned_data['document']))
            # sheetX = xls.parse(1) #2 is the sheet number
            for r in dfs.iterrows():
                id = r[1]['Student_id']
                name=r[1]['Name']
                email=r[1]['Email']
                batch=r[1]['Batch']
                branch=r[1]['Branch']
                semester=r[1]['Semester']
                students = Students.objects.create(Student_id = id,Name = name,Email = email,Batch = batch,Branch = branch,CGPA = 0,Semester = semester)  
                courses=Courses.objects.filter(Semester=semester).filter(Course_Type=0) 
                student=Students.objects.get(Student_id=id)
                for course in courses:
                    student.courses.add(course)
            return HttpResponseRedirect('/')
    else:
        form = StudentsForm()
    return render(request, 'students/student_upload.html', {
        'form': form
    })

def course_upload(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            dfs = pd.read_excel('documents/'+str(form.cleaned_data['document']))
            for r in dfs.iterrows():
                name=r[1]['Course Name']
                credits=r[1]['Course_credits']
                lectures=r[1]['Lectures']
                lab=r[1]['Lab']
                practicals = r[1]['Practicals']
                semester=r[1]['Semester']
                elective = r[1]['Course_Type']
                instructor = Instructors.objects.get(Instructor_id=r[1]['Instructor_id'])
                cid = r[1]['Course_id']
                # print(semester) 
                courses = Courses.objects.create(Course_id =cid, Course_Name = name,Course_credits = credits,Lectures =lectures,Lab=lab,Practicals=practicals,Semester=semester,Course_Type = elective,Instructor_id = instructor)
                
                # print(r[1]['Student ID'],"\n\n")      
                  
            return HttpResponseRedirect('/')
    else:
        form = CourseForm()
    return render(request, 'students/course_upload.html', {
        'form': form
    })


def Elective_upload(request):
    if request.method == 'POST':
        form = ElectiveForm(request.POST, request.FILES)
        if form.is_valid():
            student=str(form.cleaned_data['Student_id'])
            semester=str(form.cleaned_data['Semester'])  
            student=Students.objects.get(Student_id=student)
            courses=Courses.objects.filter(Semester=semester).filter(Course_Type=1)
            template = loader.get_template('students/selectelectives.html')
            context = {
                'course_entries' : courses,'student_id':student,
            }
            return HttpResponse(template.render(context,request))
    else:
        form = ElectiveForm()
    return render(request, 'students/electives.html', {
        'form': form
    })
def submit_electives(request,student_id):
    electives=request.GET.getlist('course_name')
    # print(electives)
    student=Students.objects.get(Student_id=student_id)
    semester=student.Semester
    count=0
    for elective in electives:   
        ee=Courses.objects.filter(Course_id=elective)
         
        if(count!=0):
            courses= courses | ee 
        else:
            courses= ee
            count+=1
    print(count)
    for course in courses:
        student.courses.add(course)
    return HttpResponse("fasf")

def home(request):
    return render(request, 'students/home.html', {
    })