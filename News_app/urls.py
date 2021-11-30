from django.urls import path
from .views import *

urlpatterns = [
    path('topnews/', TopNewsView.as_view(), name='topnews'),
    path('mostnews/', MostViewsView.as_view(), name='mostnews'),
    path('news/', NewsListView.as_view(), name='news'),
    path("news/<int:pk>/", NewsDetailView.as_view(), name='news_detail'),
    path('cats/', CategoriesList.as_view(), name='cats'),
    path("cats/<int:pk>/", CategoryDetail.as_view(), name='cats_detail'),
    ]

