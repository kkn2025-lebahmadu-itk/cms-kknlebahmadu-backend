from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from data.models import Gallery, News
from api.serializers import GallerySerializer, GetNewsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def home_views(request):
    response = {}

    all_news = News.objects.exclude(thumbnail__isnull=True).exclude(thumbnail="")[:3]
    news = GetNewsSerializer(all_news, many=True, context={'request': request}).data
    galeri = GallerySerializer(Gallery.objects.all()[:3], many=True, context={'request': request}).data
    user = {'id': request.user.id, 'username': request.user.username} if request.user.is_authenticated else None 

    data = {
        'news' : news,
        'galeri': galeri,
        'user': user
    }

    response['message'] = 'data honmepage berhasil diambil'
    response['data'] = data

    return Response(response, status=status.HTTP_200_OK)
    