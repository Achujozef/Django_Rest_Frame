from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Class Based API
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

class genericApiView(generics.GenericAPIView,mixins.ListModelMixin,
                      mixins.CreateModelMixin,mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    lookup_field='id'

    def get(self,request,id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request):
        return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id=None):
        return self.destroy(self,request,id)





# Class Based API
class PostAPIView(APIView):
    def get(self,request):
        post=Post.objects.all()#query Set
        serializer=PostSerializer(post,many=True)
        return Response (serializer.data)

    def post (self,request):
        serializer=PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetailsAPIView(APIView):
    def get_objt(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
          raise Http404
    def get(self,request,pk):
        post= self.get_objt(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    def put(self,request,pk):
        post= self.get_objt(pk)
        serializer = PostSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,satus=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        post= self.get_objt(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Create FUnction your views here.
 
@api_view(['GET','POST'])
def PostView (request):

    if request.method=='GET':
        post=Post.objects.all()#query Set
        serializer=PostSerializer(post,many=True)
        return Response (serializer.data)
    
    elif request.method =='POST':
   
        serializer=PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return ("Hello")
    
@api_view(['GET','PUT',"DELETE"])
def Post_Details(request,pk):
    try:
        post=Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=404)

    if request.method=='GET':
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method=='PUT':
      
        serializer = PostSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,satus=400)
    elif request.method=='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

