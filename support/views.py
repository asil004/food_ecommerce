from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import SupportSerializer

from .models import Support


class SupportListApiView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
