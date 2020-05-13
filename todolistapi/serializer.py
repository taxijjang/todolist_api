from .models import DoList,DoneList
from rest_framework import serializers

class DoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoList

        fields = ('id','title','body','published_data')

class DoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneList

        fields = ('id','title','body','published_data')