INSERT INTO Testing_ETL.[dbo].[Unificado]
SELECT
a.CHROM CHROM,
a.POS POS,
a.ID ID,
a.REF REF,
a.ALT ALT,
a.QUAL QUAL,
a.FILTER FILTER,
a.INFO INFO,
a.FORMAT FORMAT,
a.MUESTRA MUESTRA,
a.VALOR VALOR,
a.ORIGEN ORIGEN,
a.FECHA_COPIA FECHA_COPIA,
a.RESULTADO RESULTADO
FROM 
(
SELECT 
CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT, MUESTRA, VALOR, ORIGEN, GETDATE() AS FECHA_COPIA, RESULTADO
FROM [Testing_ETL].[dbo].[Unificado_stg]
) a

TRUNCATE TABLE [Testing_ETL].[dbo].[Unificado_stg]