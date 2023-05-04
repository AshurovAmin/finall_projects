# Generated by Django 4.2 on 2023-05-03 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.CharField(blank=True, max_length=12, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('number_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.ImageField(blank=True, default='profile/default-avatar.png', null=True, upload_to='profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96, verbose_name='Название')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('img', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'События',
                'verbose_name_plural': 'Событии',
            },
        ),
    ]
