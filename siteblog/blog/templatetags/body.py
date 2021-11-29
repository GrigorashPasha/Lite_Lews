from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('blog/popular_posts_body.html')
def get_popular_post(cnt=1):
    Post.created_at = timezone.now()
    posts = Post.objects.filter(
        created_at__range=[timezone.now() - timezone.timedelta(1), timezone.now()]).order_by('-views')[:cnt]
    return {"posts": posts}
