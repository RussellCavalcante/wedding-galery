from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'import_users'

urlpatterns = [
    path('import_users/', csrf_exempt(views.ImportUsers.as_view()), name='criar'),
    # path('import_usuarios_xslx/', csrf_exempt(views.Criar.as_view()), name='criar'),

]