from rest_framework import serializers

from .models import About, Workers, Positions


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ['created_at', 'updated_at']


class PostionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class WorkersSerializers(serializers.ModelSerializer):
    position = PostionSerializer(read_only=True)

    class Meta:
        model = Workers
        fields = "__all__"
