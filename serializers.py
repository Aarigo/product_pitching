from rest_framework import serializers
from .models import product,order
class product_serializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=product
		fields=['productid','productname','productprice']
class order_serializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=order
		fields=['orderno','orderdate'] 