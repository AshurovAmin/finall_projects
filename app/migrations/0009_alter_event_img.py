# Generated by Django 4.2 on 2023-05-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_avatar_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]