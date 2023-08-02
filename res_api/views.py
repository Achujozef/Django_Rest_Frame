from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
 
@csrf_exempt
def PostView (request):

    if request.method=='GET':
        post=Post.objects.all()
        serializer=PostSerializer(post,many=True)
        return JsonResponse (serializer.data,safe=False)
    
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    else:
        return ("Hello")
    
def Post_Details(request,pk):
    try:
        post=Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer=PostSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer = PostSerializer(post,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors,satus=400)
    

