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
