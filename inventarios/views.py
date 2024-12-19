from django.urls import path
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import viewsets
from .serializers import ProductoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework import serializers
from .models import Producto
from .forms import ProductoForm 


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated] # Solo usuarios autenticados puede acceder
    
    def get_object(self):
        """ 
        Sobrescribir para manejar el caso de objeto no encontrado.
        """
        try:
            return super().get_object()
        except Producto.DoesNotExist:
            raise NotFound("El producto solicitado no existe.")


# Permiso personalizado para verificar si el usuario pertenece al grupo "Admin"
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado y pertenece al grupo "Admin"
        return request.user and request.user.groups.filter(name='Admin').exists()

# Permiso personalizado para verificar si el usuario pertenece al grupo "Editor"
class IsEditor(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado y pertenece al grupo "Editor"
        return request.user and request.user.groups.filter(name='Editor').exists()

# Permiso personalizado para verificar si el usuario pertenece al grupo "Visualizador"
class IsViewer(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado y pertenece al grupo "Visualizador"
        return request.user and request.user.groups.filter(name='Visualizador').exists()


# Vista para listar productos - Solo accesible por usuarios con el rol de Visualizador
class ProductoListView(APIView):
    # Requiere autenticacion y pertenecer al grupo "Visualizador"
    permission_classes = [IsAuthenticated, IsViewer]
    
    def get(self, request):
        # Obtiene todos los productos de la base de datos
        productos = Producto.objects.all()
        # Serializa los productos a formato JSON
        serializer = ProductoSerializer(productos, many=True)
        # Devuelve la lista de productos en la respuesta
        return Response(serializer.data)

# Vista para crear productos - Solo accesible por usuarios con el rol de Editor
class ProductoCreateView(APIView):
    
    # Requiere autenticación y pertenecer al grupo "Editor"
    permission_classes = [IsAuthenticated, IsEditor]
    
    def post(self, request):
        # Convierte los datos enviados en formato JSON a un objeto Producto
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid(): # Valida los datos del serializador
            serializer.save() # Guarda el nuevo producto en la base de datos
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Vista para eliminar productos - Solo accesible por usuarios con el rol de Admin
class ProductoDeleteView(APIView):
    # Requiere autenticación y pertenecer al grupo "Admin"
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def delete(self, request, pk):
        # Busca el producto por su ID (pk). Si no existe, lanza un error 404
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete() # Elimina el producto de la base de datos
        # Devuelve una respuesta vacía con estado 204 (sin contenido)
        return Response(status=204)
    

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos')
    
    else:
        form = ProductoForm()
    return render(request, 'product_form.html', {'form': form})

def editar_producto(request, id):
    # Obtiene el producto a editar
    producto = get_object_or_404(Producto, pk=id)
    
    # Si el formulario se ha enviado 
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
    
        # Si el formulario es válido, guarda los cambios
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos') # Redirige a la lista de productos
    else:
        # Si es un GET, muestra el formulario con los datos del producto
        form = ProductoForm(instance=producto)
    
    # Muestra el formulario con los datos del producto
    return render(request, 'product_form.html', {'form': form, 'producto': producto})
    
        


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista_productos')
    return render(request, 'confirm_delete.html', {'producto':producto})