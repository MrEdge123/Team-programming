# Generated by Django 3.1.2 on 2020-11-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemsContent',
            fields=[
                ('problemId', models.AutoField(primary_key=True, serialize=False, verbose_name='problemId')),
                ('problemTitle', models.CharField(max_length=200, verbose_name='problemTitle')),
                ('memoryLimit', models.IntegerField(verbose_name='details')),
                ('timeLimit', models.IntegerField(verbose_name='input')),
                ('problemDescription', models.TextField(max_length=500, verbose_name='problemDescription')),
                ('inputDescription', models.TextField(max_length=500, verbose_name='inputDescription')),
                ('outputDescription', models.TextField(max_length=500, verbose_name='outputDescription')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemTestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemId', models.CharField(max_length=50, verbose_name='problemId')),
                ('number', models.IntegerField(verbose_name='number')),
                ('inputData', models.TextField(max_length=500, verbose_name='inputData')),
                ('outputData', models.TextField(max_length=500, verbose_name='outputData')),
                ('isExample', models.SmallIntegerField(verbose_name='isExample')),
                ('explanation', models.TextField(max_length=500, verbose_name='explanation')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitTime', models.DateTimeField(verbose_name='submitTime')),
                ('userName', models.CharField(max_length=50, verbose_name='userName')),
                ('problemId', models.CharField(max_length=50, verbose_name='problemId')),
                ('judgeResult', models.CharField(max_length=500, verbose_name='judgeResult')),
                ('usedMemory', models.CharField(max_length=100, verbose_name='usedMemory')),
                ('usedTime', models.IntegerField(verbose_name='usedTime')),
                ('language', models.CharField(max_length=50, verbose_name='language')),
                ('code', models.TextField(max_length=500, verbose_name='code')),
            ],
        ),
    ]
