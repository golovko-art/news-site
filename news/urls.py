from django.urls import path
from news import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.HomeNews.as_view(), name='index'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.NewsCategory.as_view(), name='category'),
    path('news/<int:news_id>/', views.view_news, name='view_news'),
    path('news/add_news/', views.add_news, name='add_news'),
]
