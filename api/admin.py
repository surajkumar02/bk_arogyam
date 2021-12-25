from django.contrib import admin
from .models import User,BlogModel,CommentModel,LikeModel

# Register your models here.
admin.site.register(User)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)