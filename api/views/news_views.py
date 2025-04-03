from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from data.models import User, News
from api.serializers import NewsSerializer, UserSerializer, GetNewsSerializer
from data.permissions import NewsPermissions

from django.shortcuts import get_object_or_404
from django.conf import settings

import os




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([NewsPermissions])
@parser_classes([MultiPartParser, FormParser])
def news_views(request, id=None):
    response = {}

    if request.method == 'POST':
        data = request.data.copy()
        data['poster'] = request.user.id
        
        serializer = NewsSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            print(serializer.validated_data)
            news = serializer.save()
            news.poster = request.user
            news.save()
            response['message'] = 'Berita baru sudah berhasil terbuat'
            response['data'] = {
                'title': news.title,
                'content': news.content,
                'poster': news.poster.username
            }
            return Response(response, status=status.HTTP_201_CREATED)

        response['message'] = 'Something went wrong'
        response['error'] = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if id:
            news = get_object_or_404(News, id=id)
            data = GetNewsSerializer(news, context={'request': request}).data
            response['message'] = f'Berita dengan id {id} berhasil difetch dari database'
            response['data'] = data
            return Response(response, status=status.HTTP_200_OK)
        
        # Kalo nggak ada, fetch semua berita
        all_news = News.objects.all()
        data = GetNewsSerializer(all_news, many=True, context={'request': request}).data
        response['message'] = f'Semua berita berhasil difetch dari database'
        response['data'] = data
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data
        news = get_object_or_404(News, id=id)
        if 'thumbnail' in data and news.thumbnail:
            old_image_path = os.path.join(settings.MEDIA_ROOT, str(news.thumbnail))
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
        serializer = NewsSerializer(news, data=data)
        if serializer.is_valid():
            news = serializer.save()
            response['message'] = f'Berita dengan id {id} berhasil diupdate'
            response['data'] = NewsSerializer(news).data
            return Response(response, status=status.HTTP_200_OK)
        else:
            response['message'] = 'Terjadi kesalahan'
            response['error'] = serializer.errors
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    elif request.method == 'DELETE':
        news = get_object_or_404(News, id=id)
        if news.thumbnail:
            image_path = os.path.join(settings.MEDIA_ROOT, str(news.thumbnail))
            if os.path.exists(image_path):
                os.remove(image_path)
        news.delete()

        response['messae'] = f'Berita dengan id {id} berhasil dihapus'
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)

