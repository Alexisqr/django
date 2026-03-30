from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    category = models.CharField('Категорія', max_length=250)
    slug = models.SlugField('Слаг')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    description = models.TextField('Опис', blank=True)
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    slug = models.SlugField('Слаг')
    main_page = models.BooleanField('Головна', default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='articles'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField('Фото', upload_to='photos')
    title = models.CharField('Заголовок', max_length=250, blank=True)

    def __str__(self):
        return self.title