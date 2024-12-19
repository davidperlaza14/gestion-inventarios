from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


app_name = 'productos'

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

# Rutas para la API
api_patterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
]

# Rutas para vistas basadas en templates
template_patterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar_producto')
]


urlpatterns = [
    path('api/', include(api_patterns)),
    path('', include(template_patterns)),    
]
