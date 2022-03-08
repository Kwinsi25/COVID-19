# Generated by Django 3.2.12 on 2022-03-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220308_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='caseNumber',
            field=models.IntegerField(null=True, verbose_name='Case Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=535685, unique=True, verbose_name='Case Number'),
        ),
    ]
