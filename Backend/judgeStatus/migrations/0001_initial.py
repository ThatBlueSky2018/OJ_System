# Generated by Django 3.2 on 2023-05-30 15:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusID', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('problemID', models.CharField(max_length=50)),
                ('result', models.CharField(default='System Error', max_length=500)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('testCase', models.CharField(default='unknown', max_length=500)),
                ('caseData', models.CharField(max_length=500)),
                ('outputData', models.CharField(default='', max_length=500)),
                ('userOutput', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='JudgeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(default=-1)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=50)),
                ('submitTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('judge', models.CharField(default='u', max_length=50)),
                ('code', models.TextField(max_length=200000)),
                ('testCase', models.CharField(default='0', max_length=50)),
                ('message', models.TextField(default='PENDING')),
                ('problemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
            ],
        ),
    ]
