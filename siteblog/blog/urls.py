from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('blog/add_news/', CreateNews.as_view(), name='add_news'),
    path('blog/<str:slug>/', UpdateNews.as_view(), name='update_news'),
    path('blog/<str:slug>/delete_news/', DeleteNews.as_view(), name='delete_news'),

]
