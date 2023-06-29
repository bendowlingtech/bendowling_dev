from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse

from models import Blog


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'