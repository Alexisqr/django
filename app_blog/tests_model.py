from django.test import TestCase
from django.utils import timezone
from .models import Category, Article


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            category='Innovations',
            slug='innovations'
        )

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)

        self.assertEqual(
            category.get_absolute_url(),
            '/articles/category/innovations/'
        )


class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            category='Test',
            slug='test'
        )

        Article.objects.create(
            title='Test Article',
            description='Text',
            slug='test-article',
            pub_date=timezone.now(),
            category=category
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)

        url = article.get_absolute_url()

        self.assertTrue(url.startswith('/articles/'))