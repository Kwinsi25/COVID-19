# Generated by Django 4.0.3 on 2022-03-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_20220307_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=943134, unique=True, verbose_name='Case Number'),
        ),
    ]
