# Generated by Django 2.1.5 on 2019-02-08 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestMaking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='ques',
        ),
    ]
