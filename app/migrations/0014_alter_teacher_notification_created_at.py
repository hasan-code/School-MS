# Generated by Django 4.2.1 on 2023-06-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_teacher_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_notification',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]