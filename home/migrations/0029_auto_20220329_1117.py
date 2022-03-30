# Generated by Django 3.2.12 on 2022-03-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_patient_casenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctorLastVisited',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctorVisitingTime',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Doctor Visiting Time'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=382397, unique=True, verbose_name='Case Number'),
        ),
    ]
