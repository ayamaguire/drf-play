from django.contrib.auth.models import User, Group

from rest_framework import serializers
from tf.interests import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class InterestSeralizer(serializers.Serializer):
    pass


class FriendSerializer(serializers.Serializer):
    pass
