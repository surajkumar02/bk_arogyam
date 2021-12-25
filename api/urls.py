from django.urls import path
from .views import like, Home,register,login,Blog,Blogs,Comment,Comments

urlpatterns = [
   path('s/',Home.as_view()),
   path('register/',register.as_view(),name='register'),
   path('login/',login.as_view(),name='login'),
   path('blog/',Blog.as_view()), #CR of blog.
   path('blog/<int:pk>/',Blog.as_view()), # UD of blog.
   path('blogs/',Blogs.as_view()), # Read of blogs
   path('/comment/<int:pk>',Comment.as_view()),
   path('<int:blog>/comments/',Comments.as_view()), #CR of Comments
   path('like/<int:blog>/<int:user>',like)
]
