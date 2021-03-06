# Generated by Django 2.1.3 on 2019-04-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190420_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.AlterField(
            model_name='courses',
            name='Course_Type',
            field=models.BooleanField(help_text='Tick if this is an Elective', verbose_name='Elective'),
        ),
    ]
