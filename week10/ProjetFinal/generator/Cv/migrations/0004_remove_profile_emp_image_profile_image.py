# Generated by Django 4.1.2 on 2022-10-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cv', '0003_profile_profile_profile_qualite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='emp_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
