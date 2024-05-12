from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "democrud"
urlpatterns = [
    path("post/", views.PostIndexView.as_view(), name="post.list"),
    path("post/create/", views.create_post, name="post.create"),
    path("post/update/<int:id>/", views.edit_post, name="post.update"),
    path("post/view/<int:id>/", views.read_post, name="post.view"),
    path("post/delete/<int:id>/", views.delete_post, name="post.delete"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
]