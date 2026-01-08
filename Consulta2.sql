-- Conectar EMPLEADOS
ALTER TABLE empleados
ADD CONSTRAINT fk_emp_cargo FOREIGN KEY (cargo_id) REFERENCES cargos(cargo_id),
ADD CONSTRAINT fk_emp_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id);

-- Conectar PRODUCTOS
ALTER TABLE productos
ADD CONSTRAINT fk_prod_prov FOREIGN KEY (proveedor_id) REFERENCES proveedores(proveedor_id),
ADD CONSTRAINT fk_prod_cat FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id);

-- Conectar ORDENES
ALTER TABLE ordenes
ADD CONSTRAINT fk_ord_cli FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
ADD CONSTRAINT fk_ord_emp FOREIGN KEY (empleado_id) REFERENCES empleados(empleado_id),
ADD CONSTRAINT fk_ord_suc FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id),
ADD CONSTRAINT fk_ord_pago FOREIGN KEY (metodo_pago_id) REFERENCES metodos_pago(metodo_id);

-- Conectar DETALLES
ALTER TABLE detalles_orden
ADD CONSTRAINT fk_det_orden FOREIGN KEY (orden_id) REFERENCES ordenes(orden_id),
ADD CONSTRAINT fk_det_prod FOREIGN KEY (producto_id) REFERENCES productos(producto_id);