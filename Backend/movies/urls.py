from django.urls import path
from .views import MoviesViewSet,UserApiView
urlpatterns = [
    path('movies', MoviesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('movies/<str:pk>', MoviesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user',UserApiView.as_view())
    ]