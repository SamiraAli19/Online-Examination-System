# Generated by Django 4.0.6 on 2022-08-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oes', '0009_mcqsubmission_issubmitted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqsubmission',
            name='obtainedMarks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='microvivasubmission',
            name='obtainedMarks',
            field=models.IntegerField(default=0),
        ),
    ]
