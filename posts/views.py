from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', {'posts' : posts})

def post_detail(request,id):
  post = Post.objects.get(id = id)
  context = {'post': post, 'titulo': post.titulo, 'corpo': post.corpo, 'criado': post.criado, 'category': post.category}
  return render(request, 'posts/detail.html', context)