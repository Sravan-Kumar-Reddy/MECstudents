from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('course_id', 'document','instructor_id', )



class NameForm(forms.Form):
    your_id = forms.CharField(label='Please Enter your Student ID', max_length=100)

class StudentsForm(forms.ModelForm):
    class Meta:
        model = StudentsDocument
        fields = ('document',)

class CourseForm(forms.ModelForm):
    class Meta:
        model = CoursesDocument
        fields = ('document',)

class ElectiveForm(forms.Form):
    Student_id = forms.CharField(label='Please Enter your Student ID', max_length=100)
    Semester = forms.CharField(label='Please Enter your Semester', max_length=100)
        