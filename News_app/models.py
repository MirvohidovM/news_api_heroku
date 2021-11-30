from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'
        ordering = ['-created_at']

    def __str__(self):
        return self.title




