# Generated by Django 4.2.1 on 2023-06-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_attendance_save_attendance_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_save',
            name='attendance_status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]