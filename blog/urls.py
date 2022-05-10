from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/', views.LikeView.as_view(), name='like_comment'),
    path('dislike/', views.DislikeView.as_view(), name='dislike_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
]
