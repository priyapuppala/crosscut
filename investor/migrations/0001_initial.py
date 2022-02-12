# Generated by Django 3.2.3 on 2021-05-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'investors',
            },
        ),
        migrations.CreateModel(
            name='InvestorContact',
            fields=[
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'investorcontact',
            },
        ),
        migrations.CreateModel(
            name='InvestorProfile',
            fields=[
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=100)),
                ('history', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=400)),
                ('pimage', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'investorprofile',
            },
        ),
    ]