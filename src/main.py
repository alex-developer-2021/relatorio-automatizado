import csv

arquivo = "../data/vendas.csv"

total_vendas = 0
total_itens = 0

with open(arquivo, newline="", encoding="utf-8") as csvfile:
    leitor = csv.DictReader(csvfile)

    for linha in leitor:
        quantidade = int(linha["quantidade"])
        valor = float(linha["valor"])

        total_itens += quantidade
        total_vendas += quantidade * valor

print("Resumo Operacional")
print("-------------------")
print(f"Total de itens vendidos: {total_itens}")
print(f"Faturamento total: R$ {total_vendas:.2f}")
