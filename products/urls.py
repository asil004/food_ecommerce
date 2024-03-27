from django.urls import include
from rest_framework.urls import path
from .views import *

urlpatterns = [
    path('product/', include([
        path('category/', ProductCategoryViewSet.as_view()),
        path('flash-sales/', Flashsalesproduct.as_view()),
        path('best-selling/', BestSellingProduct.as_view()),
        path('our/', OurProducts.as_view()),
        path('detail/', ProductDetail.as_view())
    ]))

]
