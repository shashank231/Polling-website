# Generated by Django 3.2.20 on 2024-07-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Createpoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.TextField(max_length=500, null=True)),
                ('opt1', models.CharField(max_length=100, null=True)),
                ('opt2', models.CharField(max_length=100, null=True)),
                ('opt3', models.CharField(max_length=100, null=True)),
                ('vo1', models.IntegerField(default=0, null=True)),
                ('vo2', models.IntegerField(default=0, null=True)),
                ('vo3', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
