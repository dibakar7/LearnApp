# Generated by Django 4.2.4 on 2023-11-06 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_course_notes_courses_external_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=50)),
                ('course_id', models.IntegerField(max_length=50)),
            ],
        ),
    ]
