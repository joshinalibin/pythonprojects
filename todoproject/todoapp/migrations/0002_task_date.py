# Generated by Django 4.1.5 on 2023-01-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-2-5'),
            preserve_default=False,
        ),
    ]
