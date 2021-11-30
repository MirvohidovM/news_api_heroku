from django.test import TestCase#, Client
from django.urls import reverse
from .serializers import *

# MODEL valid or invalid TESTING
# News model testing
# Category model testing
client = Client()
#News_Category_Get_TESTING
class NewsCategoryCRUDTesting(TestCase):

    def setUp(self):
        self.category_valid = Category.objects.create(name='dunyo yangiliklari')
        self.category_invalid = Category.objects.create(name="")
        self.news_valid = News.objects.create(
            title='yangiliklar',
            content='yangiliklar sahifasi',
            )
        self.news_invalid= News.objects.create(
            title='yangiliklar_2',
            content='',
            )
# News_all
    def test_get_news(self):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
#News_detail
    def test_get_news_detail(self):
        new = News.objects.get(pk=self.news_valid.pk)
        serializer = NewsSerializer(new)
        response = self.client.get(reverse('news_detail', kwargs={'pk': self.news_valid.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
#News_Valid_Post_Testing
    def test_post_new_valid(self):
        serializer = NewsSerializer(self.news_valid)
        response = self.client.post(reverse('news'), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
#News_Invalid_Post_Testing
    def test_post_new_invalid(self):
        serializer = NewsSerializer(self.news_invalid)
        response = self.client.post(reverse('news'), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
#News_Valid_Put_Testing
    def test_put_new_valid(self):
        new = News.objects.get(pk=self.news_valid.pk)
        serializer = NewsSerializer(new)
        response = self.client.put(reverse('news_detail', kwargs={'pk': self.news_valid.pk}), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
#News_Invalid_Put_Testing
    def test_put_new_invalid(self):
        new = News.objects.get(pk=self.news_invalid.pk)
        serializer = NewsSerializer(new)
        response = self.client.put(reverse('news_detail', kwargs={'pk': self.news_valid.pk}), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
#News_Valid_Delete_Testing
    def test_delete_new_valid(self):
        response = self.client.delete(reverse('news_detail', kwargs={'pk': self.news_valid.pk}))
        self.assertEqual(response.status_code, 204)
#News_Invalid_Delete_Testing
    def test_delete_new_invalid(self):
        response = self.client.delete(reverse('news_detail', kwargs={'pk': 777}))
        self.assertEqual(response.status_code, 404)
#CATEGORY
#Category_all
    def test_get_categories(self):
        categories = Category.objects.all()
        serializer = CatSerializer(categories, many=True)
        response = self.client.get(reverse('cats'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
#Category_detail
    def test_get_category(self):
        category = Category.objects.get(pk=self.category_valid.pk)
        serializer = CatSerializer(category)
        response =  self.client.get(reverse('cats_detail', kwargs={'pk': self.category_valid.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
#Category_Valid_Post_Testing
    def test_post_category_valid(self):
        serializer = CatSerializer(self.category_valid)
        response = self.client.post(reverse('cats'), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
#Category_Invalid_Post_Testing
    def test_post_category_invalid(self):
        serializer = CatSerializer(self.category_invalid)
        response = self.client.post(reverse('cats'), data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
#Category_Valid_Put_Testing
    def test_put_category_valid(self):
        cat = Category.objects.get(pk=self.category_valid.pk)
        serializer = CatSerializer(cat)
        response = self.client.put(reverse('cats_detail', kwargs={'pk': self.category_valid.pk}),
                                       data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
#Category_Invalid_Put_Testing
    def test_put_category_invalid(self):
        cat = Category.objects.get(pk=self.category_invalid.pk)
        serializer = CatSerializer(cat)
        response = self.client.put(reverse('cats_detail', kwargs={'pk': self.category_invalid.pk}),
                                       data=serializer.data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
#Category_Valid_Delete_Testing
    def test_delete_category_valid(self):
        response = self.client.delete(reverse('cats_detail', kwargs={'pk': self.category_valid.pk}))
        self.assertEqual(response.status_code, 204)
#Category_Invalid_Delete_Testing
    def test_delete_category_invalid(self):
        response = self.client.delete(reverse('cats_detail', kwargs={'pk': 50}))
        self.assertEqual(response.status_code, 404)


