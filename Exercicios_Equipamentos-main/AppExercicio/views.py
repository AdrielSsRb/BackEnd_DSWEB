from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PositionAPIView(APIView):
    def post(self, request):
        #recebe o json do criente
        PositionJson = request.data
        #converter json em python
        PositionSerialized = PositionSerializer(data=PositionJson)
        #verifica se conversão é valida!
        PositionSerialized.is_valid(raise_exception=True)
        #salva no banco de dados
        PositionSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=PositionSerialized.data)

    def get(self, request, positionId = ''):
        if positionId == '':
            PositionFound = Position.objects.all()
            serializer = PositionSerializer(PositionFound, many=True)
            return Response(serializer.data)
        try:    
            PositionFound = Position.objects.get(id=positionId)
            serializer = PositionSerializer(PositionFound, many=False)
            return Response(serializer.data)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Position not found!!')