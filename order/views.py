from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializers
from rest_framework.response import Response


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

# class OrderCreateView(APIView):
#     def get(self, request):
#         checkout = Order.objects.all().values()
#         return Response({'posts': OrderSerializers(checkout, many=True).data})
#
#
# class OrderPostView(APIView):
#     def post(self, request):
#         try:
#             serializer = OrderSerializers(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'post': serializer.data})
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class OrderPutView(APIView):
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Put not allowed"})
#         try:
#             instance = Order.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = OrderSerializers(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class OrderDeleteView(APIView):
#     def delete(self, request, pk):
#         try:
#             instance = Order.objects.get(pk=pk)
#             instance.delete()
#             return Response({'success': 'Object deleted successfully'})
#         except Order.DoesNotExist:
#             return Response({'error': 'Object does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
