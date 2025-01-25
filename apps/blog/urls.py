from django.urls import path
from .views import PostListView, PostDetailView, PostFormCategory

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', PostFormCategory.as_view(), name='post_by_category'),
]