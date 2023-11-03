# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Photos, CommentPhotos

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ["imagem", "nome", "usuario_dono", "visivel"]


class CommentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPhotos
        fields = ["photos", "nome", "comentario", "visivel"]