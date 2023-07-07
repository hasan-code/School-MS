# Generated by Django 4.2.1 on 2023-07-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_attendance_attendance_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study_Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/study_materials')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.class')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.session')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.subject')),
            ],
        ),
    ]
