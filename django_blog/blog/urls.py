from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog_home"),
    path('/user/posts/<str:username>', views.UserPostListView.as_view(), name="user_posts"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post/create/', views.PostCreateView.as_view(), name="post_create"),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
    path('about/', views.about, name="blog_about"),
]