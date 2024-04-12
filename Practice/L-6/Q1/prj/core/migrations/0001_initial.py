# Generated by Django 5.0.2 on 2024-04-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('marks_eng', models.IntegerField()),
                ('marks_chem', models.IntegerField()),
                ('marks_phy', models.IntegerField()),
            ],
        ),
    ]
