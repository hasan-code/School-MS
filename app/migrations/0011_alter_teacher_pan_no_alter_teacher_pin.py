# Generated by Django 4.2.1 on 2023-06-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_teacher_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='pan_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pin',
            field=models.PositiveIntegerField(),
        ),
    ]