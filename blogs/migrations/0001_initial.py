# Generated by Django 3.1.2 on 2021-02-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=70)),
                ('cardesc', models.CharField(max_length=255)),
                ('carimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
