# Generated by Django 3.1.2 on 2020-10-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='title',
            field=models.CharField(default='Mr.', max_length=20),
        ),
    ]
