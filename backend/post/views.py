
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class PostView(APIView):
    parser = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        post_serializer = PostSerializer(data = request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(post_serializer.data, status = status.HTTP_400_BAD_REQUEST)
    

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


       

