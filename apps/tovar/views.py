from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class TovarListView(generics.ListAPIView):
    serializer_class = TovarSerializer
    queryset = Tovar.objects.all()
