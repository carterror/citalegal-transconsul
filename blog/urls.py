from django.urls import path
from blog import views

urlpatterns = [
    
    path('', views.PostList.as_view(), name='blog'),
    path('crear', views.PostCreate.as_view(), name='post_create'),
    path(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post'),
]
