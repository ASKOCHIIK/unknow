from rest_framework import serializers
from .models import *


class TovarImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = TovarImage
        fields = ['id', 'img']


class TovarSerializer(serializers.ModelSerializer):
    img = TovarImgSerializers(many=True, read_only=True)

    class Meta:
        model = Tovar
        fields = ['id', 'title', 'price', 'img']