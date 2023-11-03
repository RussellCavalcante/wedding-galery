from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'perfil'

urlpatterns = [
    path('criar/', csrf_exempt(views.Criar.as_view()), name='criar'),
    # path('import_usuarios_xslx/', csrf_exempt(views.Criar.as_view()), name='criar'),

]