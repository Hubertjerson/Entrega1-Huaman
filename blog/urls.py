from django.urls import path
from .views import blog_post, home,create_blog,about

urlpatterns = [
    path('', home,name='home'),
    path('blog/', blog_post,name='blog_post'),
    path('blogcrear/', create_blog,name='create_blog'),
    path('about/', about,name='about'),
]
