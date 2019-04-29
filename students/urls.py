from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listall', views.index, name='listall'),
    path('<int:Student_id>',views.cgpa,name = 'cgpa'),
    path('instructor/<int:Instructor_id>',views.grade,name = 'grade'),
    path('grade',views.model_form_upload),
    path('listgrades',views.get_details),
    path('insertstudents',views.student_upload),
    path('insertcourses',views.course_upload),
    path('elec',views.Elective_upload),
    path('electives/<student_id>',views.submit_electives),
    path('update_gpa',views.update_gpa),
    path('student_home',views.student_home),
]