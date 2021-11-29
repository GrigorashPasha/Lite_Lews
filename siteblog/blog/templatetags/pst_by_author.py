from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/post_by_author.html')
def get_author_post():
    posts = Post.objects.filter(author=4)
    return {"posts": posts}

