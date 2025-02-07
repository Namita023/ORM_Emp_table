# Generated by Django 5.0.6 on 2024-07-12 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=30)),
                ('loc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.FloatField()),
                ('comm', models.FloatField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
