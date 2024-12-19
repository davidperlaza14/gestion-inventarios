from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'cantidad']
    
    def validate_precio(self, value):
        """
        Validar que el precio sea un valor positivo.
        """
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value
    
    def validate_cantidad(self, value):
        """
        Validar que la cantidad sea un número entero positivo.
        """
        if value < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")
        return value