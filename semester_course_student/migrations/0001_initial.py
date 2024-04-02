# Generated by Django 5.0.3 on 2024-04-02 13:28

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semester_course', '0002_alter_semestercourse_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterCourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('mid_term', models.IntegerField(blank=0)),
                ('final', models.IntegerField(blank=True, null=True)),
                ('make_up', models.IntegerField(blank=True, null=True)),
                ('semester_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_course_students', to='semester_course.semestercourse')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_course_students', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Semester Course Student',
                'verbose_name_plural': 'Semester Course Students',
                'db_table': 'semester_course_student',
                'ordering': ['-created_at'],
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]