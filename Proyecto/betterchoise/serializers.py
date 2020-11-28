from django.contrib.auth.models import User, Group
from betterchoise.models import Search
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        field = ['brand','model','price_max','price_min','page','use','category']
