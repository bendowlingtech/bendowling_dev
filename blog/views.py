from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from django.http import HttpResponse

from models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('list')






