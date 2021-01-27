from rest_framework import serializers
from Product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    folio = serializers.CharField()
    descripcion    = serializers.CharField()
    costo = serializers.CharField()
    cantidad =  serializers.IntegerField()
    
    def create(self, validate_data):
        instance = Product()
        instance.folio = validate_data.get('folio')
        instance.descripcion = validate_data.get('descripcion')
        instance.costo = validate_data.get('costo')
        instance.cantidad = validate_data.get('cantidad')
        instance.save()
        return instance
    class Meta:
        model = Product
        fields = ('__all__')