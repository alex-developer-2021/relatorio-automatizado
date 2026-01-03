def calcular_media(valores):
    if not valores:
        return 0

    total = sum(valores)
    quantidade = len(valores)

    return total / quantidade