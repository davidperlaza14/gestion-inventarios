from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']
    
    # Validación personalizada para el campo "nombre"
    def clean_nombre(self):
        """
        Valida que el nombre del producto no contenga caracteres especiales ni números.
        """
        nombre = self.cleaned_data.get('nombre')  # Obtiene el valor del campo nombre
        
        # Verifica si el nombre contiene algo que no sean letras o espacios
        if not nombre.replace(" ", "").isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras y espacios.")
        
        return nombre  # Devuelve el valor validado

    # Validación personalizada para el campo "descripcion"
    def clean_descripcion(self):
        """
        Valida que la descripción tenga al menos 10 caracteres.
        """
        descripcion = self.cleaned_data.get('descripcion')  # Obtiene la descripción
        
        # Verifica la longitud mínima
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        
        return descripcion  # Devuelve el valor validado

    # Validación personalizada para el campo "precio"
    def clean_precio(self):
        """
        Valida que el precio sea un número positivo mayor que 0.
        """
        precio = self.cleaned_data.get('precio')  # Obtiene el valor del precio
        
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        
        return precio  # Devuelve el valor validado

    # Validación personalizada para el campo "cantidad"
    def clean_cantidad(self):
        """
        Valida que la cantidad sea un número mayor o igual a 0.
        """
        cantidad = self.cleaned_data.get('cantidad')  # Obtiene el valor de cantidad
        
        if cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa.")
        
        return cantidad  # Devuelve el valor validado
























"""
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']
        
    
    
    def clean_price(self):
        # Obtiene el precio ingresado en el formulario
        price = self.cleaned_data.get('precio')
        # Valida que el precio sea mayor que 0
        if price <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return price

    def clean_quantity(self):
        # Obtiene la cantidad ingresada en el formulario
        quantity = self.cleaned_data.get('cantidad')
        # Valida que la cantidad sea mayor o igual a 0
        if quantity < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa.")
        return quantity
        
"""