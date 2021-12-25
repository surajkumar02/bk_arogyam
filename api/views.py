from django.db import models
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import User,BlogModel,CommentModel,LikeModel
from .serializers import CommentSerializer, UserSerializer,BlogSerializer
from rest_framework.views import APIView, Response,status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import (
        CreateAPIView, DestroyAPIView,
        GenericAPIView, ListAPIView,UpdateAPIView )
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator


# Create your views here.
def like(request,blog=None,user=None):
    return HttpResponse("Data is here")

class Home(APIView):
    def get(self,request):
        return Response("Data of class Home")

class login(APIView):
    def post(self,request):
        if request.data:
            try:
                username=request.data['username']
                password=request.data['password']
                useravail=User.objects.get(username=username)
                if useravail.password==password:   
                    token=RefreshToken.for_user(useravail)
                    return Response(data={"author":useravail.name,
                    "email":useravail.email,
                    "token":{"refresh":str(token),
                    "access":str(token.access_token)}
                    })
                return Response("Incorrect Password",status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
            except:
                return Response("Incompleted format",status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        return Response("Enter Valid Credentials",status=status.HTTP_404_NOT_FOUND)

class register(APIView):
    def post(self,request):
        username=request.data["username"]
        password=request.data['password']
        name=request.data['name']

        useravail=UserSerializer(data=request.data)
        if useravail.is_valid():
            user=User.objects.create(username=username,email=username,name=name)
            user.password=password
            user.save()

            token=RefreshToken.for_user(user)
            return Response(data={"author":user.name,
            "email":user.username,
            "token":{"refresh":str(token),
            "access":str(token.access_token)}})

        content="user already Exists"
        return Response(content,status=status.HTTP_406_NOT_ACCEPTABLE)

class Blog(CreateAPIView,UpdateAPIView,DestroyAPIView,GenericAPIView):

    permission_classes=[IsAuthenticated]
    
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializer

    def get(self,request):
        user=request.data['user']
        comments=CommentModel.objects.all()
        blog=BlogModel.objects.filter(user=user)
        result=[]
        for i in blog:
            print(i)
            result.append({'blog_id':i.blog_id,'blog':i.blog, 'likes':i.like,'comments':i.comment})
        

        return Response(data=(result,comments))

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,*kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class Blogs(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        page=request.data['page']
        blogs=BlogModel.objects.all()
        blog=[]
        for i in blogs:
            comment=[]
            comments=CommentModel.objects.filter(blog=i.blog_id)
            x={
                'blog':i.blog,
                'author':i.user.name,
                'likes':i.like,
                'comments':i.comments
            }
            for j in comments:
                y={
                    'comment':j.comment,
                    'by':j.user.name,
                    'liked':False
                }
                comment.append((y))
            blog.append((x,y))
        paginator=Paginator(blog,5)
        result=paginator.get_page(page)
        return Response(data={"blog":list(blog)})

class Comment(CreateAPIView,UpdateAPIView,DestroyAPIView,GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    queryset=CommentModel.objects.all()
    serializer_class=CommentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Comments(ListAPIView,):

    def get(self,request,blog=None):
        page=request.data['page']
        blog=BlogModel.objects.get(blog_id=blog)
        comments=CommentModel.objects.filter(blog=blog)
        comment=[]
        for i in comments:
            res={
                'comment':i.comment,
                'by':i.user.name,
                'liked':False
            }
            comment.append(res)
        paginator=Paginator(comment,5)
        result=paginator.get_page(page)
        return Response(data={"blog":blog.blog,"comments":list(result)})