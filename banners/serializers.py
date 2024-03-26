from rest_framework import serializers

from .models import Banners


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = "__all__"
