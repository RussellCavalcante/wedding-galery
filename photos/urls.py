from django.urls import path
from .views import (PhotoApiView,)


app_name = 'photos'

urlpatterns = [
    # path('listar_imagens/', csrf_exempt(views.ListaPhotos.as_view()), name='listar'),
     path('listar_imagens/', PhotoApiView.as_view({"get": "list"})),
     path('create_imagens/', PhotoApiView.as_view({"post": "create"})),
     path('listar_comentarios/', PhotoApiView.as_view({"get": "listComment"})),
     path('create_comentarios/', PhotoApiView.as_view({"post": "createComment"})),
    # path('create_imagem/', csrf_exempt(views.insert_photo()), name='criar'),
]

