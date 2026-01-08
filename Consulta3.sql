SELECT 
    o.fecha AS Fecha_Venta,
    suc.nombre AS Sucursal,
    emp.nombre AS Vendedor,
    cli.nombre AS Cliente,
    cat.nombre AS Categoria,
    prod.nombre AS Producto,
    det.cantidad AS Cantidad,
    det.precio_venta AS Precio_Unitario,
    (det.cantidad * det.precio_venta) AS Total_Venta
FROM ordenes o
JOIN detalles_orden det ON o.orden_id = det.orden_id
JOIN clientes cli ON o.cliente_id = cli.cliente_id
JOIN empleados emp ON o.empleado_id = emp.empleado_id
JOIN sucursales suc ON o.sucursal_id = suc.sucursal_id
JOIN productos prod ON det.producto_id = prod.producto_id
JOIN categorias cat ON prod.categoria_id = cat.categoria_id
LIMIT 20;