# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
#If you tell the database to bring back something that's not in the database, it will give you a 404.
#You'll either type in a slug that matches an article or you'll get a failure page.
from schick.blog.models import Blog, Post

########## THE BASICS ###########

def blog_index(request, blog_slug):
    """
    List view
    """
    bloginfo = Blog.objects.all()

    feed = Post.objects.all().order_by('-publication_date')

    return render_to_response('blog.html', {'feed':feed, 'bloginfo': bloginfo})


def blog_detail(request, blog_slug, slug):
    """
    Detail view for individual blog posts.
    """
    post = Post.objects.get(slug=slug)
    
    return render_to_response('blog_detail.html', {'post': post})
'''
def blog_detail(request, slug):
    """
    Detail view for individual blog posts.
    """
    post = Post.objects.get(slug=slug)
    #post = get_object_or_404(blog.post_class, publication_date__year=year,
                            # publication_date__month=month, publication_date__day=day,
                            # slug=post_slug, status='1', publication_date__lte=datetime.datetime.now())
    return render_to_response('blog_detail.html', {'post': post})
'''
