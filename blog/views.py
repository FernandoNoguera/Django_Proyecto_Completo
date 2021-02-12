from django.shortcuts import render

from blog.models import Post, Categoria

def blog(request):
    posteos = Post.objects.all()
    context = {'posteos':posteos}

    return render(request, 'blog/blog.html', context)


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posteos = Post.objects.filter(categorias=categoria)
    context = {'posteos':categoria, 'posteos':posteos}

    return render(request, 'blog/categoria.html', context)

