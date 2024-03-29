# Generated by Django 4.1.5 on 2023-04-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('account_type', models.CharField(choices=[('A', 'select Account'), ('S', 'Savings'), ('C', 'Current'), ('L', 'Loan'), ('F', 'Fixed')], max_length=1)),
                ('materials_required', models.CharField(max_length=50)),
            ],
        ),
    ]
