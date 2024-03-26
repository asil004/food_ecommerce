from rest_framework import generics

from .serializers import AboutSerializer, WorkersSerializers
from .models import About, Workers


class AboutListAPIView(generics.ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()


class WorkersListAPIView(generics.ListAPIView):
    serializer_class = WorkersSerializers
    queryset = Workers.objects.select_related('position').all()
