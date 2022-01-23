# Generated by Django 4.0.1 on 2022-01-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_employee_department_employee_counternumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='counterNumber',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='counter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]