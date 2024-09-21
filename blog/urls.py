from django.urls import path
from blog import views

urlpatterns = [
    
    # path('', views.PostList.as_view(), name='blog'),
    # path('crear', views.PostCreate.as_view(), name='post_create'),
    # path(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post'),

    path('admincitas/blog/', views.blog, name='blog'),
    path('admincitas/blog/store/', views.storeBlog, name='storeBlog'),
    path('admincitas/blog/<int:pk>/update/', views.updateBlog, name='updateBlog'),
    path('admincitas/blog/<int:pk>/delete/', views.deleteBlog, name='deleteBlog'),
    path('admincitas/blog/delete-all/', views.deleteAllBlog, name='deleteAllBlog'),

]
