# Generated by Django 2.2.6 on 2019-10-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191031_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='summary',
            field=models.CharField(default='SUMMARY UNKNOWN', max_length=128),
        ),
    ]
