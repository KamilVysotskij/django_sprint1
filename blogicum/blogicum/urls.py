from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('posts/', include('blog.urls', namespace='posts')),
    path('category/', include('blog.urls', namespace='category')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]