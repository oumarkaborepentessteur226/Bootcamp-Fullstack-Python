# Generated by Django 4.1.2 on 2022-10-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cv', '0004_remove_profile_emp_image_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='default', upload_to='upload/'),
            preserve_default=False,
        ),
    ]
