# Generated by Django 3.0.5 on 2024-04-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0023_course_exam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='entry_time',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='exam_date',
            field=models.DateTimeField(),
        ),
    ]
