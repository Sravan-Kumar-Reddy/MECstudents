# Generated by Django 2.1.3 on 2019-04-21 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_remove_studentsdocument_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesdocument',
            name='Course_id',
        ),
    ]
