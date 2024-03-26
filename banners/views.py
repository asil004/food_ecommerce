from rest_framework import generics

from .serializers import BannerSerializers
from .models import Banners


class BannerListAPIView(generics.ListAPIView):
    serializer_class = BannerSerializers
    queryset = Banners.objects.all()
