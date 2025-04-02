from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from data.models import Gallery, News
from data.permissions import Gallerypermissions
from api.serializers import GallerySerializer, NewsSerializer

from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([Gallerypermissions])
@parser_classes([MultiPartParser, FormParser])
def gallery_views(request, id=None):
    response = {}
    if request.method == 'GET':
        gallery_images = Gallery.objects.all()
        # news_images = News.objects.exclude(thumbnail=False)
        news_images = News.objects.exclude(thumbnail__isnull=True).exclude(thumbnail="")

        # Serialize data
        gallery_data = GallerySerializer(gallery_images, many=True, context={'request': request}).data
        news_data = NewsSerializer(news_images, many=True, context={'request': request}).data

        # Combine all image data into one response
        response['message'] = 'Semua gambar dari berbagai model berhasil diambil'
        response['data'] = {
            'gallery_images': gallery_data,
            'news_images': news_data
        }

        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['message'] = 'Berhasil menambahkan gambar ke galeri'
            return Response(response, status=status.HTTP_200_OK)
        
        response['message'] = 'Terjadi kesalahan'
        response['errors'] = serializer.errors

        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        data = get_object_or_404(Gallery, id=id)
        data.delete()

        response['message'] = 'Berhasil menghapus gambar dari galeri'

        return Response(response, status=status.HTTP_204_NO_CONTENT)