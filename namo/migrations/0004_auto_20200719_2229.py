# Generated by Django 3.0.6 on 2020-07-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0003_remove_createpoll_qnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpoll',
            name='vo1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='createpoll',
            name='vo2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='createpoll',
            name='vo3',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
