# Generated by Django 3.1.2 on 2021-02-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210227_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='carimage',
            field=models.ImageField(default='', upload_to='blogs/images'),
        ),
    ]
