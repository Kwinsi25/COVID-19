# Generated by Django 4.0.3 on 2022-03-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_configuration_alter_appointment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=997837, unique=True, verbose_name='Case Number'),
        ),
    ]
