# 🚀 Enterprise ERP Data Warehouse & Analytics

## 📋 Descripción del Proyecto
Diseño e implementación de una infraestructura de datos completa (Data Warehouse) simulando un entorno de Retail Corporativo. El sistema gestiona la ingesta de datos de Logística, RRHH y Ventas, soportando cargas masivas de información.

Este proyecto demuestra el ciclo completo de Ingeniería de Datos: **ETL (Extracción, Transformación y Carga)**, **Modelado Relacional** y **Analítica SQL Avanzada**.

## 🛠️ Tech Stack & Herramientas
* **Python 3.x:** Orquestación de scripts y lógica de negocio.
* **Pandas:** Transformación de datos y DataFrames.
* **MySQL Server 8.0:** Motor de base de datos y almacenamiento.
* **SQLAlchemy:** ORM y conector de base de datos.
* **Faker:** Generación de datos sintéticos (+25,000 registros con integridad referencial).

## 🏗️ Arquitectura de Datos
El sistema consta de **10 Tablas Relacionales** bajo un esquema normalizado, incluyendo:
* **Tablas de Hechos:** `ordenes`, `detalles_orden`.
* **Dimensiones:** `clientes`, `productos`, `empleados`, `sucursales`, `proveedores`.

## 📊 Analítica SQL (Business Intelligence)
El repositorio incluye scripts SQL (`analisis_avanzado.sql`) que resuelven problemas de negocio reales:
1.  **Ranking de Vendedores:** Uso de Window Functions (`DENSE_RANK`, `PARTITION BY`) para medir desempeño por sede.
2.  **Principio de Pareto (80/20):** Identificación de productos clave.
3.  **Time Intelligence:** Análisis de tendencias de ventas mensuales.

## 🚀 Cómo ejecutar este proyecto
1.  Clonar el repositorio.
2.  Instalar dependencias:
    ```bash
    pip install pandas sqlalchemy pymysql faker
    ```
3.  Configurar credenciales de MySQL en `generar_erp.py`.
4.  Ejecutar el script ETL:
    ```bash
    python generar_erp.py
    ```
5.  Analizar los datos resultantes en MySQL Workbench.

---
*Desarrollado como práctica de Ingeniería de Datos Avanzada.*