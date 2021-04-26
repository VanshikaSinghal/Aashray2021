# Generated by Django 3.1.5 on 2021-04-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aashray', '0002_contact_answered'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlasmaDonorForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.CharField(max_length=13, unique=True)),
                ('bloodGroup', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], default='A+', max_length=3)),
                ('address', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('prevDonation', models.CharField(max_length=150)),
                ('antibodies', models.CharField(max_length=150)),
                ('medIssues', models.TextField(max_length=500)),
                ('answered', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]