# Generated by Django 4.1.3 on 2022-11-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='slug',
        ),
    ]
