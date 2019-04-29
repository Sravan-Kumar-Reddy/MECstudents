from django.contrib import admin

# Register your models here.

from .models import Students, Instructors,Courses, Grades


admin.site.register(Students)
admin.site.register(Instructors)
admin.site.register(Courses)

class GradesAdmin(admin.ModelAdmin):

    fields = (
        'Student_id',
        'Course_id',
        'Grade',
        'CoursesList(Student_id)'
    )
    courses = []
    def CoursesList(Student_id):
        for i in Students.objects.all():
            if(i.Student_id == Student_id):
                courses.append(i.courses.all())


#admin.site.register(Grades,GradesAdmin)
admin.site.register(Grades)