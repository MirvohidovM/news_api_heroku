from rest_framework import serializers
from .models import News, Category

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"