from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
import json
from rest_framework import status
import pandas as pd
from io import StringIO, BytesIO
import codecs
import requests

    
class ImportUsers(View):

    def post(self, request, *args, **kwargs):
        
        uploaded_file = request.FILES['data']
        
        destination = open(f'media/{uploaded_file.name}', 'wb+')
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
        destination.close()
        
        df = pd.read_csv(f'media/{uploaded_file.name}', delimiter=';', header=None)
        json_list = []

            # Itera sobre as linhas do DataFrame
        for index, row in df.iterrows():
            # Converte a linha para um dicionário
            data_dict = {
                'username': row[0],
                'email': row[1],
                'password': row[2],
                'last_name': row[3]
            }
            
            # Converte o dicionário em JSON e adiciona à lista
            json_data = json.dumps(data_dict)
            json_list.append(json_data)
            
        # Agora json_list contém os JSONs correspondentes a cada linha do DataFrame
        for json_data in json_list:
            json_object = json.loads(json_data)
            if User.objects.filter(username=json_object['username']):
                data=json.loads("""{"Error":"usuario ja existe !"}""")
                break
                # return HttpResponse([data] ,status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(json_object['username'], json_object['email'], json_object["password"])
            user.last_name = json_object["last_name"]
            user.save()
        
        return HttpResponse([json_data], status=status.HTTP_201_CREATED)

