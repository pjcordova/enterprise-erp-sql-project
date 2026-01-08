SELECT * FROM (
    SELECT 
        suc.nombre AS Sucursal,
        emp.nombre AS Vendedor,
        SUM(det.cantidad * det.precio_venta) AS Total_Vendido,
        -- Aquí está la magia: Rankeamos REINICIANDO la cuenta en cada sucursal
        DENSE_RANK() OVER (
            PARTITION BY suc.nombre 
            ORDER BY SUM(det.cantidad * det.precio_venta) DESC
        ) AS Ranking
    FROM ordenes o
    JOIN detalles_orden det ON o.orden_id = det.orden_id
    JOIN empleados emp ON o.empleado_id = emp.empleado_id
    JOIN sucursales suc ON o.sucursal_id = suc.sucursal_id
    GROUP BY suc.nombre, emp.nombre
) AS Ranking_Table
WHERE Ranking = 1; -- Solo mostramos al #1 de cada sede

SELECT 
    prod.nombre AS Producto,
    cat.nombre AS Categoria,
    SUM(det.cantidad * det.precio_venta) AS Ventas_Totales,
    COUNT(*) AS Veces_Vendido
FROM detalles_orden det
JOIN productos prod ON det.producto_id = prod.producto_id
JOIN categorias cat ON prod.categoria_id = cat.categoria_id
GROUP BY prod.nombre, cat.nombre
ORDER BY Ventas_Totales DESC
LIMIT 10; -- Top 10 productos estrella


SELECT 
    DATE_FORMAT(o.fecha, '%Y-%m') AS Mes_Anio,
    COUNT(DISTINCT o.orden_id) AS Total_Transacciones,
    ROUND(SUM(det.cantidad * det.precio_venta), 2) AS Ingresos_Totales
FROM ordenes o
JOIN detalles_orden det ON o.orden_id = det.orden_id
WHERE o.fecha >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) -- Últimos 12 meses
GROUP BY DATE_FORMAT(o.fecha, '%Y-%m')
ORDER BY Mes_Anio;