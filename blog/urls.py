from django.urls import path
from blog import views as viewBlog

urlpatterns = [
    
    # path('', views.PostList.as_view(), name='blog'),
    # path('crear', views.PostCreate.as_view(), name='post_create'),
    # path(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post'),

    path('', viewBlog.blog, name='blog'),
    path('store/', viewBlog.storeBlog, name='storeBlog'),
    path('<int:pk>/update/', viewBlog.updateBlog, name='updateBlog'),
    path('<int:pk>/delete/', viewBlog.deleteBlog, name='deleteBlog'),
    path('delete-all/', viewBlog.deleteAllBlog, name='deleteAllBlog'),

]
