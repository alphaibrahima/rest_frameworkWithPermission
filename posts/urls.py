from nturl2path import url2pathname
from django.urls import URLPattern, path
from .views import PostList, PostDetail


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]