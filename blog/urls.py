from .views import PostList, post_detail
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='blog_post_list'),
    path('<int:year>/<int:month>/<slug:slug>', post_detail, name='blog_post_detail')
]