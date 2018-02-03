from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #this filters the blog posts on publush date in the past and orders them by date
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #this gives back the post_list html under blog
    return render(request, 'blog/post_list.html', {'posts': posts})
