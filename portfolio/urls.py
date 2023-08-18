
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/list', views.BlogListView, name='list'),
    path('/detail', views.BlogDetailView, name='detail'),
    path('/create', views.BlogCreateView, name='create'),
]