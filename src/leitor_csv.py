import csv

def ler_vendas(caminho_arquivo):
    vendas = []

    with open(caminho_arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)

        for linha in leitor:
            vendas.append({
                "quantidade": int(linha["quantidade"]),
                "valor": float(linha["valor"])
            })

    return vendas
