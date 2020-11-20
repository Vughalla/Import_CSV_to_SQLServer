DELETE FROM Testing_ETL.dbo.Unificado
WHERE fecha_copia NOT IN 
(
SELECT MAX(fecha_copia) AS maxFecha
FROM Testing_ETL.dbo.Unificado
GROUP BY id, muestra, resultado
)