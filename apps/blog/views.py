from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def home(request):
    # posts = Post.objects.all()
    # return render(request, 'home/home.html', {'posts' : posts})
    return render(request, 'home/home.html')

    # dj_database_url