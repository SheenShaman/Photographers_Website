import datetime

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100, verbose_name='Slug', **NULLABLE)
    content = models.TextField(verbose_name='Контент', **NULLABLE)
    image = models.ImageField(upload_to='photo/', verbose_name='Фотографии', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime.utcnow)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
