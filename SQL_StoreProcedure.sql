DELIMITER //

CREATE PROCEDURE sp_reporte_ventas_sucursal(
    IN nombre_sucursal VARCHAR(100),
    IN fecha_inicio DATE,
    IN fecha_fin DATE
)
BEGIN
    SELECT 
        s.nombre AS Sucursal,
        COUNT(o.orden_id) AS Total_Ordenes,
        SUM(d.cantidad * d.precio_venta) AS Ingresos_Totales
    FROM ordenes o
    JOIN detalles_orden d ON o.orden_id = d.orden_id
    JOIN sucursales s ON o.sucursal_id = s.sucursal_id
    WHERE s.nombre = nombre_sucursal 
      AND o.fecha BETWEEN fecha_inicio AND fecha_fin
    GROUP BY s.nombre;
END //

DELIMITER ;


CALL sp_reporte_ventas_sucursal('Sede Central Lima', '2023-01-01', '2025-12-31');