from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from data.models import LetterRecap
from api.serializers import LetterRecapSerializer

from data.permissions import RecapPermissions


@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([RecapPermissions])
def recap_views(request, id=None):
    response = {}
    if request.method == 'GET':
        all_recaps = LetterRecapSerializer(LetterRecap.objects.all(), many=True, context={'request': request}).data

        response['recaps'] = all_recaps

        return Response(response, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        try:
            if not id:
                response['message'] = f"Tidak ada id surat yang diberikan"
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            recap = LetterRecap.objects.get(id=id)
            recap.delete()

            response['message'] = f'Berhasil menghapus rekap surat dengan id {id}'

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response['message'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == "POST":
        try:
            recap = LetterRecapSerializer(data=request.data)
            if recap.is_valid():
                recap.save()
                response['message'] = 'Rekap baru sudah berhasil terbuat'
                return Response(response, status=status.HTTP_201_CREATED)

            response['errors'] = recap.errors
            return Response(response, status=status.HTTP_500_OK)
        except Exception as e:
            response['error'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)