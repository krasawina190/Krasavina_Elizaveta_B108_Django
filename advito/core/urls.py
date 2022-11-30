from .views import index, categories
from django.urls import path, re_path

urlpatterns = [
    path('1/', index, name='index'),
    path('2/', categories, name='categories'),
]