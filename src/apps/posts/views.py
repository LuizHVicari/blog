from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.exceptions import BadRequest
from django.utils.translation import gettext

from .models import Post, PostType

post_types = [t[0] for t in PostType.choices ]

def post(request, pk: int, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)


def portfolio(request, *args, **kwargs):
    posts = get_list_or_404(Post, post_type=PostType.PORTFOLIO)
    context = {
        'posts': posts
    }
    return render(request, 'posts/post-list.html', context)


def get_post_list(request, *args, **kwargs):
    post_type = request.GET.get('type')
    if post_type not in post_types:
        raise BadRequest(gettext('Could not find this post type.'))
    
    posts = get_list_or_404(Post.objects.order_by('-updated_at'), post_type=post_type)
    context = {
        'posts': posts
    }

    print(context)

    return render(request, 'posts/post-list.html', context)
