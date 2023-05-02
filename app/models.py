import datetime

from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Event(models.Model):
    title = models.CharField('Название', max_length=20)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата')
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class EventGroup(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    join_date = models.DateField()
    leave_data = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='article')

    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группы'

    def is_active(self):
        if self.leave_data < datetime.datetime.now().date():
            return False
        return True

    # def save(self, *args, **kwargs):
    #     if not self.user_id:
    #         self.user = User.objects.first()  # или какая-то другая логика
    #     super().save(*args, **kwargs)


class Profile(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.CharField(max_length=12)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')
    avatar = models.ImageField(default='profile/default-avatar.png', upload_to='profile')

    def __str__(self):
        return self.name

    # def is_active(self):
    #     if self.leave_data < datetime.datetime.now().date():
    #         return False
    #     return True
