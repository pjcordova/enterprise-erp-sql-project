USE empresa_mediana_db;

-- 1. Primero, aseguramos que los IDs no sean nulos y sean Primary Keys
ALTER TABLE sucursales MODIFY sucursal_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE cargos MODIFY cargo_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE metodos_pago MODIFY metodo_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE categorias MODIFY categoria_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE proveedores MODIFY proveedor_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE clientes MODIFY cliente_id BIGINT NOT NULL PRIMARY KEY;

-- 2. Tablas principales (Empleados y Productos)
ALTER TABLE empleados MODIFY empleado_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE productos MODIFY producto_id BIGINT NOT NULL PRIMARY KEY;

-- 3. Tabla de Hechos (Ordenes y Detalles)
ALTER TABLE ordenes MODIFY orden_id BIGINT NOT NULL PRIMARY KEY;
ALTER TABLE detalles_orden MODIFY detalle_id BIGINT NOT NULL PRIMARY KEY;