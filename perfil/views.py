from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
import json
from rest_framework import status

    
class Criar(View):

    def post(self, *args, **kwargs):
        data = self.request.body.decode()
        json_object = json.loads(data)
        if User.objects.filter(username=json_object['username']):
            data=json.loads("""{"Error":"usuario ja existe !"}""")
            return HttpResponse([data] ,status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(json_object['username'], json_object['email'], json_object["password"])
        user.last_name = json_object["last_name"]
        user.save()
        return HttpResponse([json_object], status=status.HTTP_201_CREATED)
    
    # def post(self, *args, **kwargs):
    #     data = self.request.body.decode()
    #     json_object = json.loads(data)
    #     if User.objects.filter(username=json_object['username']):
    #         data=json.loads("""{"Error":"usuario ja existe !"}""")
    #         return HttpResponse([data] ,status=status.HTTP_400_BAD_REQUEST)
    #     user = User.objects.create_user(json_object['username'], json_object['email'], json_object["password"])
    #     user.last_name = json_object["last_name"]
    #     user.save()
    #     return HttpResponse([json_object], status=status.HTTP_201_CREATED)


