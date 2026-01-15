# 🏭 Enterprise ERP: Cloud Data Warehouse & Analytics

![Postgres](https://img.shields.io/badge/Database-PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Cloud-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Python](https://img.shields.io/badge/ETL-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)

## 📋 Descripción del Proyecto
Diseño e implementación de una infraestructura de datos corporativa (**Data Warehouse**) simulando un entorno de Retail a gran escala. 

El sistema gestiona la ingesta masiva de datos de Logística y Ventas, soportando un ciclo completo de **Ingeniería de Datos Moderna**:
1.  **Ingesta (ETL):** Generación de datos sintéticos (+10,000 transacciones) con integridad referencial estricta usando Python & Faker.
2.  **Almacenamiento Cloud:** Migración de arquitectura local a **Supabase (PostgreSQL)** para alta disponibilidad.
3.  **Lógica de Negocio:** Implementación de Triggers y Funciones en base de datos para auditoría automática.
4.  **Consumo:** Visualización de KPIs financieros en tiempo real.

---

## 🏗️ Arquitectura de Datos (Schema Design)

El sistema utiliza un esquema normalizado (cercano a un **Snowflake Schema**) optimizado tanto para la integridad transaccional (OLTP) como para consultas analíticas (OLAP).

### 🗺️ Diagrama Entidad-Relación (ERD)

```mermaid
erDiagram
    SUCURSALES ||--|{ ORDENES : genera
    CLIENTES ||--|{ ORDENES : realiza
    EMPLEADOS ||--|{ ORDENES : gestiona
    ORDENES ||--|{ DETALLES_ORDEN : contiene
    PRODUCTOS ||--|{ DETALLES_ORDEN : listado_en
    CATEGORIAS ||--|{ PRODUCTOS : clasifica
    PROVEEDORES ||--|{ PRODUCTOS : suministra

    ORDENES {
        int id PK
        date fecha
        int cliente_id FK
        int sucursal_id FK
    }
    DETALLES_ORDEN {
        int orden_id FK
        int producto_id FK
        float precio_venta
        int cantidad
    }
