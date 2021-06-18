from app.views import *
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('images/<id>', image_detail, name="image_detail"),
    path('category/<id>', category, name="category"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
