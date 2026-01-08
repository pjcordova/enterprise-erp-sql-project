CREATE TABLE historial_precios (
    historial_id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    precio_antiguo DECIMAL(10,2),
    precio_nuevo DECIMAL(10,2),
    fecha_cambio DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER before_precio_update
BEFORE UPDATE ON productos
FOR EACH ROW
BEGIN
    IF OLD.precio_unitario <> NEW.precio_unitario THEN
        INSERT INTO historial_precios (producto_id, precio_antiguo, precio_nuevo)
        VALUES (OLD.producto_id, OLD.precio_unitario, NEW.precio_unitario);
    END IF;
END //

DELIMITER ;

-- 1. Actualizamos un precio
UPDATE productos SET precio_unitario = precio_unitario + 50 WHERE producto_id = 1;

-- 2. Revisamos si el espía lo anotó
SELECT * FROM historial_precios;