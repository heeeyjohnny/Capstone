# Generated by Django 3.0.4 on 2020-03-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiftswap', '0002_auto_20200312_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='pay',
            field=models.FloatField(default=0.0),
        ),
    ]
