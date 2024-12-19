# Gestión de Productos

Este proyecto es una aplicación web para gestionar productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) con una interfaz gráfica moderna y responsiva. Está construido con **Django**, aprovechando sus capacidades robustas para desarrollo web.

---

## **Instrucciones de Instalación y Uso**

### **Requisitos Previos**
- Python 3.8 o superior.
- Entorno virtual (recomendado).
- pip para la instalación de paquetes.

### **Pasos para Instalar**

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/usuario/gestion-productos.git
   cd gestion-productos
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos:**
   - Por defecto, el proyecto utiliza SQLite.
   - Migrar las bases de datos:
     ```bash
     python manage.py migrate
     ```

5. **Ejecutar el servidor local:**
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación:**
   - Abra su navegador y visite: [http://localhost:8000](http://localhost:8000)

---

## **Estructura del Proyecto**

```
.
├── gestion_productos
│   ├── migrations/       # Migraciones de base de datos
│   ├── static/           # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/        # Plantillas HTML
│   ├── models.py         # Definición de modelos (Producto)
│   ├── forms.py          # Formularios con validaciones personalizadas
│   ├── views.py          # Lógica de vistas CRUD
│   └── urls.py           # Rutas de la aplicación
├── db.sqlite3            # Base de datos SQLite (por defecto)
├── manage.py             # Comando de gestión de Django
├── README.md             # Documentación del proyecto
└── requirements.txt      # Lista de dependencias
```

---

## **Funcionalidades Implementadas**

### **1. Operaciones CRUD**
- **Crear Producto:**
  - Formulario para agregar nuevos productos con validaciones personalizadas.
  - Alertas visuales de éxito y error.
- **Editar Producto:**
  - Actualización de productos existentes con validaciones y diseño intuitivo.
- **Eliminar Producto:**
  - Confirmación antes de eliminar un producto.
  - Mensajes de feedback al usuario.
- **Listar Productos:**
  - Tabla responsiva que muestra los productos con opciones para editar o eliminar.

### **2. Validaciones en Formularios**
- El precio debe ser mayor a 0.
- La cantidad no puede ser negativa.

### **3. Estética y Usabilidad**
- Interfaz gráfica moderna basada en **Bootstrap**.
- Mensajes de alerta y navegación intuitiva.
- Diseño responsivo compatible con dispositivos móviles.

---

## **Créditos**
- **Desarrollador Principal:** David Perlaza.
- **Email:** davidperlaza14@gmail.com
- **Framework:** Django.
- **Diseño UI:** Bootstrap.

---

## **Reflexiones Sobre el Proyecto**

Este proyecto fue una excelente oportunidad para aplicar conocimientos en **Django** y mejorar habilidades en diseño de interfaces gráficas. Durante el desarrollo:
- Se enfrentaron y resolvieron desafíos relacionados con validaciones personalizadas y diseño responsivo.
- Se mejoró la organización del código y la estructura general del proyecto.
- Se priorizó la experiencia del usuario (UX) para garantizar una aplicación funcional y atractiva.

Este proyecto puede expandirse fácilmente, integrando nuevas funcionalidades como:
- Soporte para imágenes de productos.
- Paginación en la lista de productos.
- API REST para integrar con aplicaciones móviles.

¡Gracias por revisar este proyecto! 🚀
