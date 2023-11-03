from rest_framework.response import Response
from rest_framework import status

from .models import Photos
from .models import CommentPhotos
from .serializers import PhotoSerializer , CommentPhotoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

class PhotoApiView(ModelViewSet):
    serializer_class = PhotoSerializer
    serializer_class_comment = CommentPhotoSerializer

    pagination_class = None
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']


    def list(self, request, *args, **kwargs):
    
        photos = Photos.objects.filter(visivel = True)
        
        serializer = PhotoSerializer(photos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        data = {
            'imagem': request.data.get('imagem'), 
            'nome': request.data.get('nome'), 
            'usuario_dono': request.data.get('usuario_dono'),
            'visivel': request.data.get('visivel'), 
        }
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def listComment(self, request, *args, **kwargs):
    
        commentphotos = CommentPhotos.objects.filter(visivel = True)
        serializer = CommentPhotoSerializer(commentphotos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def createComment(self, request, *args, **kwargs):

        data = {
            'photos': request.data.get('photos'), 
            'nome': request.data.get('nome'), 
            'comentario': request.data.get('comentario'),
            'visivel': request.data.get('visivel'), 
        }
        serializer = CommentPhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)