from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

from .models import Post, Tag
from .serializers import PostSerializer


def _get_post(pk=None):
    """
    Fetch a post by its pk and raise a not found error
    if it is not found.
    """
    try:
        return Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound()


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    post = serializer.save()

    for tag_id in request.data.get('tags'):
        try:
            tag = Tag.objects.get(id=tag_id)
            post.tags.add(tag)
        except Tag.DoesNotExist:
            raise NotFound()

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_post(request, pk=None):
    post = _get_post(pk=pk)
    serializer = PostSerializer(instance=post)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_post(request, pk=None):
    post = _get_post(pk=pk)
    tags = []

    for tag_id in request.data.get('tags'):
        try:
            tag = Tag.objects.get(id=tag_id)
            tags.append(tag)
        except:
            raise NotFound()

    post.tags.set(tags)

    serializer = PostSerializer(instance=post)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
