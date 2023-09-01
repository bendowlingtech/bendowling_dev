
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/list', views.PostListView, name='list'),
    path('/detail', views.PostDetailView, name='detail'),
    path('/create', views.PostCreateView, name='create'),

]