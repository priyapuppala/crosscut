# Generated by Django 3.2.3 on 2021-05-15 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprenuer',
            fields=[
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'entreprenuers',
            },
        ),
        migrations.CreateModel(
            name='EntreprenuerContact',
            fields=[
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'entreprenuercontact',
            },
        ),
        migrations.CreateModel(
            name='EntreprenuerIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobileno', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('ideaname', models.CharField(max_length=100)),
                ('ideadesc', models.CharField(max_length=100)),
                ('ideacat', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=400)),
                ('invmail', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
            ],
            options={
                'db_table': 'entreprenuerideas',
            },
        ),
    ]
