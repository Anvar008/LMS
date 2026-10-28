from django.urls import path
from .views import *

urlpatterns = [
    path('news/', get_news, name='news'),
    path('news/category/add/', add_news_category, name='add_news_category'),
    path('news/add/', add_news, name='add_news'),
]
