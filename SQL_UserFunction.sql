DELIMITER //

CREATE FUNCTION obtener_nivel_ventas(total_vendido DECIMAL(10,2)) 
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE nivel VARCHAR(20);

    IF total_vendido > 50000 THEN
        SET nivel = '🔥 MASTER';
    ELSEIF total_vendido > 10000 THEN
        SET nivel = '⭐ SENIOR';
    ELSE
        SET nivel = '🌱 JUNIOR';
    END IF;

    RETURN (nivel);
END //

DELIMITER ;



SELECT 
    nombre, 
    salario, 
    obtener_nivel_ventas(salario * 12) AS Nivel_Proyectado 
FROM empleados 
LIMIT 10;