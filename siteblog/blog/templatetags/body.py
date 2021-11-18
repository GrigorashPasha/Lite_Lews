from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/popular_posts_body.html')
def get_popular_post(cnt=1):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}
