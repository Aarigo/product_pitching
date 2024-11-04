from rest_framework import viewsets
from .models import product,order
from .serializers import product_serializers,order_serializers
class productviewset(viewsets.ModelViewSet):
	queryset=product.objects.all()
	serializer_class=product_serializers
class orderviewset(viewsets.ModelViewSet):
	queryset=order.objects.all()
	serializer_class=order_serializers  