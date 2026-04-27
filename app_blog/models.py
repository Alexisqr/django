from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(
        'Категорія',
        max_length=250,
        help_text='Максимум 250 символів'
    )
    slug = models.SlugField('Слаг')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            return reverse(
                'articles-category-list',
                kwargs={'slug': self.slug}
            )
        except:
            return "/"



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

    def get_absolute_url(self):
      return reverse(
        'news-detail',
        kwargs={
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'day': self.pub_date.day,
            'slug': self.slug
        }
    )


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