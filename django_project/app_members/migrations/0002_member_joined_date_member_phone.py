# Generated by Django 5.2 on 2025-05-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
