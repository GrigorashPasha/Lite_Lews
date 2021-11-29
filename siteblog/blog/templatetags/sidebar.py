from django import template
from blog.models import Post, Tag
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=4):
    Post.created_at = timezone.now()
    posts = Post.objects.filter(
        created_at__range=[timezone.now() - timezone.timedelta(1), timezone.now()]).order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
