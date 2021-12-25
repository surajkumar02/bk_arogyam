from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    blog_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    blog=models.TextField(max_length=600)
    like=models.IntegerField(default=0)
    comment=models.IntegerField(default=0)

    def __str__(self):
        return self.user.name

class CommentModel(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.CharField(max_length=250)
    blog=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.blog.title} {self.user.name}')

class LikeModel(models.Model):
    id=models.AutoField(primary_key=True)
    blog=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name