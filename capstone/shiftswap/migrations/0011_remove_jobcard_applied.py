# Generated by Django 3.0.4 on 2020-03-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shiftswap', '0010_jobcard_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcard',
            name='applied',
        ),
    ]
