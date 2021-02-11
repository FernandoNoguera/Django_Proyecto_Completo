from django.shortcuts import render

from blog.models import Post

def blog(request):
    posteos = Post.objects.all()
    context = {'posteos':posteos}

    return render(request, 'blog/blog.html', context)


