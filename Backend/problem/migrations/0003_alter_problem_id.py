# Generated by Django 3.2 on 2023-06-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_alter_problem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
