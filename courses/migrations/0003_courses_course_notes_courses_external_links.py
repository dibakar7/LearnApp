# Generated by Django 4.2.4 on 2023-11-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_course_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_notes',
            field=models.FileField(blank=True, null=True, upload_to='notes/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='external_links',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
