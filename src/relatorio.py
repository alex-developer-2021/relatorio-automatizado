def gerar_resumo(vendas):
    total_itens = 0
    total_vendas = 0

    for venda in vendas:
        total_itens += venda["quantidade"]
        total_vendas += venda["quantidade"] * venda["valor"]

    return total_itens, total_vendas
