import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# --- CONFIGURACIÓN ---
DB_USER = 'root'
DB_PASSWORD = ''  # Pon tu contraseña si tienes
DB_HOST = 'localhost'
DB_NAME = 'empresa_mediana_db'


def conectar_db():
    """Crea la conexión a MySQL usando SQLAlchemy"""
    conexion_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    return create_engine(conexion_url)


def generar_graficos():
    engine = conectar_db()
    sns.set_theme(style="whitegrid")  # Estilo profesional

    print("🚀 Generando Dashboard de Analítica...")

    # --- GRÁFICO 1: TOP 10 PRODUCTOS (BARRAS) ---
    print("   -> Creando gráfico de Top Productos...")
    query_top = """
    SELECT p.nombre, SUM(d.cantidad) as total_vendido
    FROM detalles_orden d
    JOIN productos p ON d.producto_id = p.producto_id
    GROUP BY p.nombre
    ORDER BY total_vendido DESC
    LIMIT 10;
    """
    df_top = pd.read_sql(query_top, engine)

    plt.figure(figsize=(12, 6))
    # CORRECCIÓN 1: Agregamos hue y legend=False para evitar el FutureWarning
    sns.barplot(data=df_top, x='total_vendido', y='nombre',
                hue='nombre', palette='viridis', legend=False)
    # CORRECCIÓN 2: Quitamos emojis para evitar error de fuente
    plt.title('Top 10 Productos Mas Vendidos', fontsize=16)
    plt.xlabel('Unidades Vendidas')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('grafico_top_productos.png')
    plt.close()

    # --- GRÁFICO 2: VENTAS MENSUALES (LÍNEA) ---
    print("   -> Creando gráfico de Tendencia Mensual...")
    # CORRECCIÓN CRÍTICA: Usamos %% en lugar de % para que Python no se confunda
    query_trend = """
    SELECT DATE_FORMAT(o.fecha, '%%Y-%%m') as mes, SUM(d.cantidad * d.precio_venta) as ingresos
    FROM ordenes o
    JOIN detalles_orden d ON o.orden_id = d.orden_id
    GROUP BY mes
    ORDER BY mes;
    """
    df_trend = pd.read_sql(query_trend, engine)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_trend, x='mes', y='ingresos',
                 marker='o', color='b', linewidth=2.5)
    plt.title('Evolucion de Ingresos Mensuales', fontsize=16)
    plt.xticks(rotation=45)
    plt.xlabel('Mes')
    plt.ylabel('Ingresos ($)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('grafico_tendencias.png')
    plt.close()

    # --- GRÁFICO 3: HEATMAP SUCURSAL vs CATEGORÍA ---
    print("   -> Creando Mapa de Calor (Heatmap)...")
    query_heatmap = """
    SELECT s.nombre as sucursal, c.nombre as categoria, SUM(d.cantidad * d.precio_venta) as ventas
    FROM ordenes o
    JOIN detalles_orden d ON o.orden_id = d.orden_id
    JOIN sucursales s ON o.sucursal_id = s.sucursal_id
    JOIN productos p ON d.producto_id = p.producto_id
    JOIN categorias c ON p.categoria_id = c.categoria_id
    GROUP BY s.nombre, c.nombre;
    """
    df_heat = pd.read_sql(query_heatmap, engine)

    df_pivot = df_heat.pivot(
        index='sucursal', columns='categoria', values='ventas')

    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, annot=False, cmap="YlGnBu", linewidths=.5)
    plt.title('Mapa de Calor: Ventas por Sucursal y Categoria', fontsize=16)
    plt.tight_layout()
    plt.savefig('grafico_heatmap.png')
    plt.close()

    print("✅ ¡Dashboard generado! Revisa las 3 imágenes PNG en tu carpeta.")


if __name__ == "__main__":
    generar_graficos()
