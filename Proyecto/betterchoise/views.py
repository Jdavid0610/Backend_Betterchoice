from django.http import HttpResponse, JsonResponse
from betterchoise.models import Search
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bs4 import BeautifulSoup
import requests
#API Rest imports

from django.contrib.auth.models import User, Group
from rest_framework.decorators import APIView
from rest_framework import viewsets
from rest_framework import permissions
from betterchoise.serializers import UserSerializer, GroupSerializer, SearchSerializer
#API Rest
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

#paginitas personales


class searchClass(viewsets.ModelViewSet):
    @csrf_exempt
    def salu2(request):
        data=JSONParser().parse(request)
        return JsonResponse(data)

    @csrf_exempt
    def Amazon_search(request):
        #amazon search
        data=JSONParser().parse(request)
        search=data["model"]
        Price_filter_min=0
        Price_filter_max=data["price_max"]
        use_bussines=False
        use_gamer=False
        use_personal=False
        print(search+" "+str(Price_filter_max))
        #URLs de busqueda
        AlkostoURL='https://www.alkosto.com/salesperson/result/?q='+str(search)
        AmazonURLGeneral='https://www.amazon.com/s?k='+str(search)+'&i=specialty-aps&srs=20574825011&__mk_es_US=ÅMÅŽÕÑ&ref=nb_sb_noss'
        AmazonURLPriceFilter="https://www.amazon.com/s?k="+str(search)+"&rh=p_36%3A"+str(Price_filter_min)+"-"+str()+"&qid=1605228093&rnid=2421885011&ref=sr_nr_p_36_6"

        #headers
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.323'}
        
        #amaz Scraping
        Amaz = requests.get(AmazonURLPriceFilter,headers=headers)
        Amazon=BeautifulSoup(Amaz.text,'html.parser')
        imgAmz=Amazon('img')
        for a in imgAmz:
            print(a.get('src'))
        
        #alkos scraping
        alk=requests.get(AlkostoURL,headers=headers)
        Alkosto=BeautifulSoup(alk.text,'html.parser')
        imgAlk=Alkosto.select('.product-image')
        imgs=imgAlk('img')
        for a in imgs:
            print(a.get('src'))

        url={
            'brand':data["brand"],
            'model':data["model"],
            'price_max':data["price_max"],
            'URL':AlkostoURL
        }
        return JsonResponse(url)



def index(request):
    return JsonResponse({'mensaje':'soy el backed en django'})


    
