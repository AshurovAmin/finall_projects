from django.db import models
from django.db.models.signals import post_save

from user.models import User


class Event(models.Model):
    name = models.CharField('Название', max_length=96)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата')
    img = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'Событии'


class Profile(models.Model):
    username = models.CharField(max_length=20)
    birth_date = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    number_phone = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(default='profile/default-avatar.png', upload_to='profile', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
