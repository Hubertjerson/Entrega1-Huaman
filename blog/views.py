
from datetime import datetime
from django.shortcuts import redirect, render
from blog.forms import formBlog, busquedaAuthor
from blog.models import Blog, Games
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def create_blog(request):

    if request.method == 'POST':
        form = formBlog(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            fecha = data.get('fecha_creacion')

            if not fecha:
                fecha = datetime.now()
            post = Blog(
                title=data.get('title'),
                author=data.get('author'),
                contenido=data.get('contenido'),
                fecha_creacion=fecha
            )
            post.save()
            return redirect('blog_post')
        else:
            return render(request, 'crearBlog.html', {'form': form})
    blog = formBlog()

    return render(request, 'crearBlog.html', {'form': blog})


def blog_post(request):

    busqueda_author = request.GET.get('author')

    if busqueda_author:
        post = Blog.objects.filter(author__icontains=busqueda_author)
    else:
        post = Blog.objects.all()

    posts = busquedaAuthor()
    return render(request, 'blogPost.html', {'post': post, 'posts': posts})

def games(request):
    juegos = Games.objects.all()
    return render(request, 'games.html', {'juegos': juegos})