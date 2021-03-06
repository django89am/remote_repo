# Generated by Django 2.0 on 2020-01-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_fee', models.IntegerField()),
                ('institute_name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
    ]
