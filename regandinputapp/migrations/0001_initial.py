# Generated by Django 4.2.7 on 2023-11-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=15)),
                ('LastName', models.CharField(max_length=15)),
                ('UserName', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=15)),
                ('CPassword', models.CharField(max_length=15)),
                ('EmailID', models.EmailField(max_length=254)),
                ('MobileNo', models.IntegerField()),
            ],
        ),
    ]
