from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from data.models import User, News
from api.serializers import NewsSerializer, UserSerializer, GetNewsSerializer
from data.permissions import NewsPermissions

from django.shortcuts import get_object_or_404





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
        news.delete()

        response['messae'] = f'Berita dengan id {id} berhasil dihapus'
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# @permission_classes([AdminOnly])
# @parser_classes([MultiPartParser, FormParser])
# def create_news(request):
#     response = {}

#     data = request.data.copy()
#     data['poster'] = request.user.id
    
#     print(data)

#     serializer = NewsSerializer(data=data, context={'request': request})
#     if serializer.is_valid():
#         print(serializer.validated_data)
#         news = serializer.save()
#         news.poster = request.user
#         news.save()
#         response['message'] = 'Berita baru sudah berhasil terbuat'
#         response['data'] = {
#             'title': news.title,
#             'content': news.content,
#             'poster': news.poster.username
#         }
#         return Response(response, status=status.HTTP_201_CREATED)

#     response['message'] = 'Something went wrong'
#     response['error'] = serializer.errors
#     return Response(response, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_news(request, id=None):
#     response = {}

#     # fetch 1 berita aja kalo ada id di url
#     if id:
#         news = get_object_or_404(News, id=id)
#         data = GetNewsSerializer(news, context={'request': request}).data
#         response['message'] = f'Berita dengan id {id} berhasil difetch dari database'
#         response['data'] = data
#         return Response(response, status=status.HTTP_200_OK)
    
#     # Kalo nggak ada, fetch semua berita
#     all_news = News.objects.all()
#     data = GetNewsSerializer(all_news, many=True, context={'request': request}).data
#     response['message'] = f'Semua berita berhasil difetch dari database'
#     response['data'] = data
#     return Response(response, status=status.HTTP_200_OK)



# @api_view(['PUT'])
# @permission_classes([AdminOnly])
# def update_news(request, id):
#     response = {}
#     data = request.data
#     news = get_object_or_404(News, id=id)
#     serializer = NewsSerializer(news, data=data)
#     if serializer.is_valid():
#         news = serializer.save()
#         response['message'] = f'Berita dengan id {id} berhasil diupdate'
#         response['data'] = NewsSerializer(news).data
#         return Response(response, status=status.HTTP_200_OK)
#     else:
#         response['message'] = 'Terjadi kesalahan'
#         response['error'] = serializer.errors
#         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# @api_view(['DELETE'])
# @permission_classes([AdminOnly])
# def delete_news(request, id):
#     response = {}
#     news = get_object_or_404(News, id=id)
#     news.delete()

#     response['messae'] = f'Berita dengan id {id} berhasil dihapus'
    
#     return Response(response, status=status.HTTP_204_NO_CONTENT)




