from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

from .models import Post, Tag
from .serializers import PostSerializer


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
