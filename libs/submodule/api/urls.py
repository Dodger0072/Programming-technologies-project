from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CartViewSet, OrderViewSet, FavoriteViewSet, SalesStatisticsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'sales-statistics', SalesStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]