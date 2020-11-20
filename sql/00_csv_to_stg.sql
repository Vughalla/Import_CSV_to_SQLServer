BULK INSERT Testing_ETL.[dbo].[Unificado_stg]
    FROM '$(PATH_INPUT)/$(csvFile)'
    WITH
    (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '\n',
        BATCHSIZE=30000
    )
GO
