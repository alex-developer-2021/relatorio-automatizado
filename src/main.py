from leitor_csv import ler_vendas
from relatorio import gerar_resumo

CAMINHO_CSV = "../data/vendas.csv"

vendas = ler_vendas(CAMINHO_CSV)
total_itens, total_vendas = gerar_resumo(vendas)

print("Resumo Operacional")
print("-------------------")
print(f"Total de itens vendidos: {total_itens}")
print(f"Faturamento total: R$ {total_vendas:.2f}")

from utilidades import calcular_media

valores = [10, 20, 30]
media = calcular_media(valores)

print(media)
