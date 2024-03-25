from rest_framework import generics
from .serializers import UserSerializers
from .models import User


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
