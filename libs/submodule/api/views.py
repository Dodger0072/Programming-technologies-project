from rest_framework import viewsets
from .models import User, Product, Cart, Order, Favorite, SalesStatistics
from .serializers import UserSerializer, ProductSerializer, CartSerializer, OrderSerializer, FavoriteSerializer, SalesStatisticsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class SalesStatisticsViewSet(viewsets.ModelViewSet):
    queryset = SalesStatistics.objects.all()
    serializer_class = SalesStatisticsSerializer