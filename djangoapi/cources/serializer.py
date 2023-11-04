from rest_framework import serializers
from .models import Cource

class CourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Cource
        fields = ('id','url','name','language','price')

