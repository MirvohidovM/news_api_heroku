from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class TopNewsView(views.APIView):

    def get(self, request):
        news = News.objects.filter(featured=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class MostViewsView(views.APIView):

    def get(self, request):
        news = News.objects.order_by("-views")[:3]
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class Filter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset


class NewsListView(views.APIView):
    filter_fields = ('title', 'id')
    search_fields = ('title', 'content')
    ordering_fields = ('id', 'created_at', 'views')
    # permission_classes = (AllowAny,)

    def get(self, request):
        queryset = News.objects.all()

        filter = Filter()
        filtered_queryset = filter.filter_queryset(request, queryset, self)

        if filtered_queryset.exists():
            serializer = NewsSerializer(filtered_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=NewsSerializer)
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(views.APIView):

    def get(self, request, pk):
        new = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(new)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NewsSerializer)
    def put(self, request, pk):
        new = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        new = get_object_or_404(News, pk=pk)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesList(views.APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CatSerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CatSerializer)
    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(views.APIView):
    # def get_object(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         raise Http404

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CatSerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CatSerializer)
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CatSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)