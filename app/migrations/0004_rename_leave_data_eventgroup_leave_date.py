# Generated by Django 4.2 on 2023-05-02 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventgroup',
            old_name='leave_data',
            new_name='leave_date',
        ),
    ]
