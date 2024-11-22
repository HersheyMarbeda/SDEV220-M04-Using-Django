from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.

# This is the view that will be called when the user goes to the home page
# The view will render the home page

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
