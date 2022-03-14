from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',views.PostView.as_view(), name='posts_list'),
    path('posts/<pk>',views.PostDetail.as_view()),
]