# Generated by Django 4.2.1 on 2023-06-24 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_attendance_save_attendance_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance_Save',
            new_name='Save_Attendance',
        ),
    ]