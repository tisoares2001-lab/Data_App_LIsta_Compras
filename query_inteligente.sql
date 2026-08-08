WITH tb_lag AS (
    SELECT *,
           lag(dt_compra) OVER (PARTITION BY 
           produto ORDER BY dt_compra) AS 
           dt_compra_anterior
    FROM compras
), 
tb_stats_produto AS (
    SELECT produto,
           max(dt_compra) AS dt_ultima_compra,
           avg(valor_produto) AS media_valor -- <--- 2. Vírgula extra removida daqui (não pode ter vírgula antes do FROM)
    FROM compras
    GROUP BY produto
),

tb_avg AS (
    SELECT produto,
           avg(julianday(dt_compra) - julianday(dt_compra_anterior)) AS avg_dias_entre_compras
    FROM tb_lag
    GROUP BY produto
)

SELECT t1.*, 
       t2.avg_dias_entre_compras,
       julianday('now') - julianday(t1.dt_ultima_compra) AS dias_desde_ultima_compra
FROM tb_stats_produto AS t1
LEFT JOIN tb_avg AS t2
ON t1.produto = t2.produto;