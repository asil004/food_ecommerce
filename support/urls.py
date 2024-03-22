from django.urls import path
from .views import SupportListApiView

urlpatterns = [
    path('support/', SupportListApiView.as_view())
]
