from rest_framework.urls import path
from .views import *
urlpatterns = [
    path('category-products/',ProductCategoryViewSet.as_view()),
    path('flash-sales/',Flashsalesproduct.as_view()),
    path('best-selling-products/',BestSellingProduct.as_view()),
    path('our-products/',OurProducts.as_view()),
    path('product-detail/',ProductDetail.as_view())
]