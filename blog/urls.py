from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from blog.models import PostForms

urlpatterns = [
                url(r'^$', ListView.as_view(
                                    queryset=PostForms.objects.all().order_by()[:25],
                                    template_name="blog/blog.html"), name='blog'),
                url(r'^blog/(?P<pk>\d+)/$', views.posts, name='posts'),

                url(r'postForm', views.postform, name='postform'),
                url(r'^results/$', views.search, name="search"),
                path('download/', views.blog_download, name='download')
            ]
