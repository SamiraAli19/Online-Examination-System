# Generated by Django 4.0.6 on 2022-08-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oes', '0008_rename_camdidate_mcqsubmission_candidate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcqsubmission',
            name='isSubmitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='microvivasubmission',
            name='isSubmitted',
            field=models.BooleanField(default=False),
        ),
    ]