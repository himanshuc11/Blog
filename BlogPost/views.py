from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from BlogUser.models import User
from .models import Post
from .serializers import ListSerializer, PostCreationSerializer

# Create your views here.
# Listing all the posts
class AllPostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = ListSerializer(posts, many=True)
        return Response(serializer.data)

# List all posts of a particular User
class UserPostListAPIView(APIView):
    def get(self, request, id):
        posts = Post.objects.filter(id=id)
        serializer = ListSerializer(posts, many=True)
        return Response(serializer.data)

# Create and Update Post
# Creation: User should be logged In


class CreateAPIView(APIView):
    def get(self, request):
        return Response('Please use POST or PUT')

    # Creation
    def post(self, request):
        if request.user.is_anonymous:
            return Response('Please Login To create a Post', status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        data['owner'] = request.user.id
        serializer = PostCreationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# Updation: User should be logged In and should be the post owner
class UpdateAPIView(APIView):
    def get(self, request, id):
        return Response('Please Login')

    def put(self, request, id):
        if request.user.is_anonymous:
            return Response('Please Login')

        try:
            post = Post.objects.get(id=id) # x = Post.objects.filter(id=id), if len(x) > 0:
        except Post.DoesNotExist:
            return Response('Invalid Post')

        if post.owner == request.user:
            data = request.data
            data['owner'] = request.user.id

            serializer = PostCreationSerializer(post, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('You cannot edit this post')

# Comment, User can comment on Posts