# Databricks notebook source
dados = [
    {"entrega_id": 1000,
    "data_envio": "2026-01-01",
    "data_entrega": "2026-01-20",
    "regiao": "Nordeste",
    "transportadora": "Transportadora A",
    "custo_frete": 30.00,
    "prazo_dias": 15,
    "status": "Entregue"},
    
    {"entrega_id": 1001,
    "data_envio": "2026-01-20",
    "data_entrega": "2026-01-27",
    "regiao": "Sudeste",
    "transportadora": "Transportadora B",
    "custo_frete": 8.75,
    "prazo_dias": 7,
    "status": "Não entregue"},


    {"entrega_id": 1003,
    "data_envio": "2026-02-28",
    "data_entrega": "2026-03-18",
    "regiao": "Sul",
    "transportadora": "Transportadora C",
    "custo_frete": 12.90,
    "prazo_dias": 10,
    "status": "Entregue"},

    {"entrega_id": 1004,
    "data_envio": "2026-03-18",
    "data_entrega": "2026-04-08",
    "regiao": "Norte",
    "transportadora": "Transportadora A",
    "custo_frete": 45.99,
    "prazo_dias": 20,
    "status": "Não entregue"},

    {"entrega_id": 1005,
    "data_envio": "2026-04-15",
    "data_entrega": "2026-04-25",
    "regiao": "Centro-Oeste",
    "transportadora": "Transportadora B",
    "custo_frete": 15.49,
    "prazo_dias": 10,
    "status": "Entregue"}
]

# COMMAND ----------

import pandas as pd

dados = [
    {"entrega_id": 1000,
    "data_envio": "2026-01-01",
    "data_entrega": "2026-01-20",
    "regiao": "Nordeste ",
    "transportadora": "Transportadora A",
    "custo_frete": 30.00,
    "prazo_dias": 15,
    "status_entrega": " Entregue"},
    
    {"entrega_id": 1001,
    "data_envio": "2026-01-20",
    "data_entrega": "2026-01-27",
    "regiao": "SUDEStE",
    "transportadora": None,
    "custo_frete": 8.75,
    "prazo_dias": 7,
    "status_entrega": "NÃO ENTREGUE"},

    {"entrega_id": 1003,
    "data_envio": "2026-02-28",
    "data_entrega": "2026-03-18",
    "regiao": "sul",
    "transportadora": "Transportadora C",
    "custo_frete": 0.00,
    "prazo_dias": 10,
    "status_entrega": "Entregue "},

    {"entrega_id": 1004,
    "data_envio": "2026-03-24",
    "data_entrega": "2026-04-08",
    "regiao": " NORTE",
    "transportadora": "Transportadora A",
    "custo_frete": 45.99,
    "prazo_dias": 20,
    "status_entrega": " Não entregue "},

    {"entrega_id": 1005,
    "data_envio": "2026-04-15",
    "data_entrega": "2026-04-20",
    "regiao": "Centro- Oeste",
    "transportadora": "Transportadora B",
    "custo_frete": 15.49,
    "prazo_dias": 10,
    "status_entrega": "entregue"},

    {"entrega_id": 1006,
    "data_envio": "2026-01-01",
    "data_entrega": "2026-01-30",
    "regiao": "Sul ",
    "transportadora": "Transportadora B",
    "custo_frete": 36.00,
    "prazo_dias": 10,
    "status_entrega": "  Entregue"},
    
    {"entrega_id": 1007,
    "data_envio": "2026-01-01",
    "data_entrega": "2026-01-17",
    "regiao": "SUDESte",
    "transportadora": "Transportadora A",
    "custo_frete": 6.75,
    "prazo_dias": 7,
    "status_entrega": " ENTREGUE"},

    {"entrega_id": 1008,
    "data_envio": "2026-02-08",
    "data_entrega": "2026-02-12",
    "regiao": "sUl",
    "transportadora": "Transportadora A",
    "custo_frete": 0.00,
    "prazo_dias": 10,
    "status_entrega": "Não Entregue "},

    {"entrega_id": 1009,
    "data_envio": "2026-03-14",
    "data_entrega": "2026-03-24",
    "regiao": " NORTE",
    "transportadora": "Transportadora C",
    "custo_frete": 55.59,
    "prazo_dias": 20,
    "status_entrega": " entregue"},

    {"entrega_id": 1010,
    "data_envio": "2026-04-15",
    "data_entrega": "2026-05-05",
    "regiao": "Centro-oeste ",
    "transportadora": "Transportadora C",
    "custo_frete": 25.49,
    "prazo_dias": 10,
    "status_entrega": "Não entregue"}
]

dados_dataframe = pd.DataFrame(dados)

dados_dataframe.loc[4, "regiao"] = "Centro_Oeste"
dados_dataframe.loc[2, "custo_frete"] = 12.50
dados_dataframe.loc[1, "transportadora"] = "Transportadora B"

dados_dataframe["regiao"] = dados_dataframe["regiao"].str.upper()
dados_dataframe["regiao"] = dados_dataframe["regiao"].str.strip()

dados_dataframe["status_entrega"] = dados_dataframe["status_entrega"].str.upper()
dados_dataframe["status_entrega"] = dados_dataframe["status_entrega"].str.strip()

dados_dataframe['data_envio'] = pd.to_datetime(dados_dataframe['data_envio'])
dados_dataframe['data_entrega'] = pd.to_datetime(dados_dataframe['data_entrega'])

dias_entrega = dados_dataframe["data_entrega"] - dados_dataframe["data_envio"]
dados_dataframe["dias_entrega"] = dias_entrega.dt.days

dados_dataframe.loc[
    dados_dataframe["dias_entrega"] > dados_dataframe["prazo_dias"], "status_prazo"
    ] = "ATRASADO"

dados_dataframe.loc[
    dados_dataframe["dias_entrega"] <= dados_dataframe["prazo_dias"], "status_prazo"
    ] = "NO PRAZO"

print(dados_dataframe)

contagem_status_entrega = dados_dataframe["status_entrega"].value_counts()
print(contagem_status_entrega)

contagem_status_prazo = dados_dataframe["status_prazo"].value_counts()
print(contagem_status_prazo)

porcentagem_status_entrega = dados_dataframe['status_entrega'].value_counts(normalize=True) * 100
print(porcentagem_status_entrega)

porcentagem_status_prazo = dados_dataframe['status_prazo'].value_counts(normalize=True) * 100
print(porcentagem_status_prazo)

status_entrega_transportadora = dados_dataframe.groupby('transportadora')['status_entrega'].value_counts()
print(status_entrega_transportadora)

porcentagem_status_entrega_transportadora = dados_dataframe.groupby('transportadora')['status_entrega'].value_counts(normalize=True) * 100
print(porcentagem_status_entrega_transportadora)

status_prazo_transportadora = dados_dataframe.groupby('transportadora')['status_prazo'].value_counts()
print(status_prazo_transportadora)

porcentagem_status_prazo_transportadora = dados_dataframe.groupby('transportadora')['status_prazo'].value_counts(normalize=True) * 100
print(porcentagem_status_prazo_transportadora)

dados_dataframe.to_csv("dataset_logistica_tratado.csv", index=False, encoding='utf-8', sep=',')

dataframe_spark = spark.createDataFrame(dados_dataframe)

dataframe_spark.show()

dataframe_spark.printSchema()

dataframe_spark.createOrReplaceTempView("dataset_logisticaSQL")

spark.sql(
    """SELECT * 
    FROM dataset_logisticaSQL"""
    ).show()

spark.sql(
    """SELECT 
    transportadora,
    COUNT(*) as total_entregas
    FROM dataset_logisticaSQL
    GROUP BY transportadora"""
).show()

spark.sql(
    """SELECT 
    transportadora,
    COUNT(*) AS total_entregas,
    ROUND(AVG(custo_frete),2) AS media_frete,
    SUM(
        CASE WHEN(
        status_prazo = 'ATRASADO'
        ) THEN 1 ELSE 0 
        END
    ) AS atrasos

    FROM dataset_logisticaSQL
    GROUP BY transportadora"""
).show()

taxa_atraso_transportadora = spark.sql(
    """SELECT 
    transportadora,
    COUNT(*) AS total_entregas,
    SUM(
        CASE WHEN(
        status_prazo = 'ATRASADO'
        ) THEN 1 ELSE 0 
        END
    ) AS atrasos,

    ROUND(
        SUM(
            CASE WHEN(
            status_prazo = 'ATRASADO'
            ) THEN 1 ELSE 0 
            END
        ) / COUNT(*),2
    ) * 100 AS taxa_atrasos

    FROM dataset_logisticaSQL
    GROUP BY transportadora"""
)

taxa_atraso_transportadora.show()

taxa_atraso_transportadora_pd = taxa_atraso_transportadora.toPandas()

taxa_atraso_transportadora_pd.to_csv(
    "taxa_atraso_transportadora.csv",
    index = False
)

regioes_problematicas = spark.sql(
    """SELECT 
    regiao,
    COUNT(*) AS total_entregas,
    
    AVG(dias_entrega) AS media_dias,

    SUM(
        CASE 
        WHEN(
            status_prazo = 'ATRASADO'
        ) THEN 1 
        ELSE 0 
        END
    ) AS atrasos

    FROM dataset_logisticaSQL
    GROUP BY regiao"""
)

regioes_problematicas.show()

regioes_problematicas_pd = regioes_problematicas.toPandas()

regioes_problematicas_pd.to_csv(
    "regioes_problematicas.csv",
    index = False
)

ranking_transportadoras = spark.sql(
    """SELECT 
    transportadora,
    
    ROUND(AVG(dias_entrega), 2) AS media_dias,

    ROUND(AVG(custo_frete), 2) AS media_frete

    FROM dataset_logisticaSQL
    GROUP BY transportadora
    ORDER BY media_dias ASC"""
)

ranking_transportadoras.show()

ranking_transportadoras_pd = ranking_transportadoras.toPandas()

ranking_transportadoras_pd.to_csv(
    "ranking_transportadoras.csv",
    index = False
)
