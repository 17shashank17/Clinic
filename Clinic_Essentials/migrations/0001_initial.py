# Generated by Django 2.2.4 on 2019-12-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(default='', max_length=25)),
                ('patient_number', models.CharField(default='', max_length=15)),
                ('problem_detail', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('contact', models.CharField(default='', max_length=15)),
                ('feedback', models.CharField(default='', max_length=200)),
            ],
        ),
    ]