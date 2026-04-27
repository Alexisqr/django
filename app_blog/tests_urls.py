
from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView
from .models import Category, Article
from django.utils import timezone

class HomeTests(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(
            category='Test Category',
            slug='test-category'
        )

        self.article = Article.objects.create(
            title='Test Article',
            description='Test description',
            slug='test-article',
            pub_date=timezone.now(),
            category=self.category
        )

    def test_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_resolves(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        url = reverse(
            'articles-category-list',
            kwargs={'slug': self.category.slug}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url(self):
        url = reverse(
            'news-detail',
            kwargs={
                'year': self.article.pub_date.year,
                'month': self.article.pub_date.month,
                'day': self.article.pub_date.day,
                'slug': self.article.slug
            }
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
