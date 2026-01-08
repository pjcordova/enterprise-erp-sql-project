import pandas as pd
from sqlalchemy import create_engine, text
import random
from faker import Faker
from datetime import datetime, timedelta

# --- 1. CONFIGURACIÓN DE CONEXIÓN MYSQL (ROOT / SIN PASSWORD) ---
USER = 'root'
PASSWORD = ''  # <--- VACÍO PORQUE NO TIENES CLAVE
HOST = 'localhost'
PORT = '3306'
DB_NAME = 'empresa_mediana_db'

# Cadena de conexión para que Python hable con MySQL
connection_string_server = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}"
connection_string_db = f"{connection_string_server}/{DB_NAME}"

fake = Faker('es_ES')  # Datos en español

# --- 2. PARAMETROS DE LA SIMULACIÓN ---
NUM_SUCURSALES = 5
NUM_CARGOS = 6
NUM_EMPLEADOS = 80
NUM_CLIENTES = 3000
NUM_PROVEEDORES = 40
NUM_PRODUCTOS = 200
NUM_ORDENES = 25000      # 25,000 Ventas
MAX_ITEMS = 8

print("🚀 INICIANDO GENERADOR DE ERP (EMPRESA MEDIANA)...")

# --- 3. CREAR BASE DE DATOS SI NO EXISTE ---
try:
    engine_server = create_engine(connection_string_server)
    with engine_server.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    print(f"✅ Base de datos '{DB_NAME}' verificada en MySQL.")
except Exception as e:
    print(f"❌ ERROR CRÍTICO CONECTANDO A MYSQL: {e}")
    print("   -> Asegúrate de que XAMPP/MySQL esté encendido.")
    exit()

# Nos conectamos a la base de datos específica
engine_db = create_engine(connection_string_db)

# --- 4. GENERACIÓN DE DATOS (TABLAS MAESTRAS) ---

# A. Sucursales
print("🏢 Creando 5 Sucursales...")
df_sucursales = pd.DataFrame([
    {'sucursal_id': 1, 'nombre': 'Sede Central Lima', 'ciudad': 'Lima'},
    {'sucursal_id': 2, 'nombre': 'Almacén Norte', 'ciudad': 'Trujillo'},
    {'sucursal_id': 3, 'nombre': 'Tienda Sur', 'ciudad': 'Arequipa'},
    {'sucursal_id': 4, 'nombre': 'Outlet Callao', 'ciudad': 'Callao'},
    {'sucursal_id': 5, 'nombre': 'Oficina Huancayo', 'ciudad': 'Huancayo'}
])

# B. Cargos
print("👔 Creando Jerarquía de Cargos...")
cargos_data = [
    {'cargo_id': 1, 'titulo': 'Gerente Regional', 'salario_min': 8000},
    {'cargo_id': 2, 'titulo': 'Supervisor de Tienda', 'salario_min': 4500},
    {'cargo_id': 3, 'titulo': 'Ejecutivo de Ventas Senior', 'salario_min': 3000},
    {'cargo_id': 4, 'titulo': 'Vendedor Junior', 'salario_min': 1500},
    {'cargo_id': 5, 'titulo': 'Asistente de Almacén', 'salario_min': 1200},
    {'cargo_id': 6, 'titulo': 'Pasante', 'salario_min': 930}
]
df_cargos = pd.DataFrame(cargos_data)

# C. Métodos de Pago
print("💳 Creando Métodos de Pago...")
df_metodos = pd.DataFrame([
    {'metodo_id': 1, 'nombre': 'Efectivo'},
    {'metodo_id': 2, 'nombre': 'Tarjeta de Crédito'},
    {'metodo_id': 3, 'nombre': 'Tarjeta de Débito'},
    {'metodo_id': 4, 'nombre': 'Transferencia Bancaria'},
    {'metodo_id': 5, 'nombre': 'Yape/Plin'}
])

# D. Categorías y Proveedores
print("📦 Creando Catálogo y Proveedores...")
categorias_list = ['Electrónica', 'Línea Blanca',
                   'Muebles', 'Ropa', 'Juguetes', 'Cómputo', 'Deportes']
df_categorias = pd.DataFrame(
    [{'categoria_id': i+1, 'nombre': c} for i, c in enumerate(categorias_list)])

df_proveedores = pd.DataFrame([{
    'proveedor_id': i+1,
    'empresa': fake.company(),
    'pais': fake.country()
} for i in range(NUM_PROVEEDORES)])

# E. Empleados
print(f"👥 Contratando {NUM_EMPLEADOS} Empleados...")
empleados_data = []
for i in range(NUM_EMPLEADOS):
    cargo = random.choice(cargos_data)
    empleados_data.append({
        'empleado_id': i+1,
        'nombre': fake.first_name(),
        'apellido': fake.last_name(),
        'email': fake.email(),
        'sucursal_id': random.randint(1, NUM_SUCURSALES),
        'cargo_id': cargo['cargo_id'],
        'salario': cargo['salario_min'] + random.randint(0, 2000),
        'fecha_ingreso': fake.date_between(start_date='-4y', end_date='today')
    })
df_empleados = pd.DataFrame(empleados_data)

# F. Productos
print(f"🛒 Fabricando {NUM_PRODUCTOS} Productos...")
productos_data = []
for i in range(NUM_PRODUCTOS):
    productos_data.append({
        'producto_id': i+1,
        'nombre': fake.word().capitalize() + " " + fake.word().capitalize(),
        'proveedor_id': random.randint(1, NUM_PROVEEDORES),
        'categoria_id': random.randint(1, len(categorias_list)),
        'precio_unitario': round(random.uniform(20, 3000), 2),
        'stock': random.randint(10, 500)
    })
df_productos = pd.DataFrame(productos_data)

# G. Clientes
print(f"🤝 Registrando {NUM_CLIENTES} Clientes...")
df_clientes = pd.DataFrame([{
    'cliente_id': i+1,
    'nombre': fake.name(),
    'email': fake.email(),
    'ciudad': fake.city()
} for i in range(NUM_CLIENTES)])

# --- 5. GENERACIÓN DE TRANSACCIONES (LO PESADO) ---
print(
    f"💸 Generando {NUM_ORDENES} Ventas Históricas (Paciencia, esto toma unos segundos)...")

ordenes_data = []
detalles_data = []
detalle_counter = 1
precios_map = df_productos.set_index(
    'producto_id')['precio_unitario'].to_dict()

for i in range(NUM_ORDENES):
    orden_id = i + 1
    fecha = fake.date_between(start_date='-2y', end_date='today')

    # Tabla Ordenes
    ordenes_data.append({
        'orden_id': orden_id,
        'cliente_id': random.randint(1, NUM_CLIENTES),
        'empleado_id': random.randint(1, NUM_EMPLEADOS),
        'sucursal_id': random.randint(1, NUM_SUCURSALES),
        'metodo_pago_id': random.randint(1, 5),
        'fecha': fecha,
        'estado': random.choice(['Finalizada', 'Finalizada', 'Devuelta'])
    })

    # Tabla Detalles
    num_items = random.randint(1, MAX_ITEMS)
    prods_seleccionados = random.sample(range(1, NUM_PRODUCTOS+1), num_items)

    for prod_id in prods_seleccionados:
        detalles_data.append({
            'detalle_id': detalle_counter,
            'orden_id': orden_id,
            'producto_id': prod_id,
            'cantidad': random.randint(1, 5),
            'precio_venta': precios_map[prod_id],
            'descuento': 0.0
        })
        detalle_counter += 1

df_ordenes = pd.DataFrame(ordenes_data)
df_detalles = pd.DataFrame(detalles_data)

# --- 6. GUARDADO EN MYSQL ---
print("💾 VOLCANDO DATOS A MYSQL...")

tablas = {
    'sucursales': df_sucursales,
    'cargos': df_cargos,
    'metodos_pago': df_metodos,
    'categorias': df_categorias,
    'proveedores': df_proveedores,
    'empleados': df_empleados,
    'productos': df_productos,
    'clientes': df_clientes,
    'ordenes': df_ordenes,
    'detalles_orden': df_detalles
}

for nombre, df in tablas.items():
    print(f"   -> Escribiendo tabla: {nombre}...")
    df.to_sql(nombre, engine_db, if_exists='replace', index=False)

print("\n" + "="*50)
print(f"✅ ¡PROCESO TERMINADO! Base de datos '{DB_NAME}' creada.")
print("👉 AHORA: Abre MySQL Workbench y dale a 'Refresh' en Schemas.")
print("="*50)
