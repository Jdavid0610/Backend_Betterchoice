from django.http import HttpResponse
from django.http import JsonResponse

#API Rest imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from betterchoise.serializers import UserSerializer, GroupSerializer

#API Rest
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#paginitas personales

def index(request):
    return JsonResponse({'mensaje':'soy el backed en django'})

def salu2(request):
    return JsonResponse({'mensaje':'soy el backend otra vez x2 :)'})
