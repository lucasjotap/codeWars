def adicional_limpeza():
    """Definindo funcao para limpezas adicionais."""
    acumulador = 0
    while True:
        try:
            print("Menu 3 de 3 - Adicionais de limpeza")
            val = int(input("""Deseja mais algum adicional?
            0 - Nao desejo mais nada (encerrar)
            1 - Passar 10 pecas de roupa
            2 - Limpeza de 1 forno/micro-ondas
            3 - Limpeza de geladeira/freezer
            >> """))

            if val == 1:
                acumulador += 10
            elif val == 2:
                acumulador += 20
            elif val == 3:
                acumulador += 30
            else:
                acumulador += 0
                break
        except ValueError:
            print("Valor invalido")
            continue
    return acumulador
print("Preço final da funcao: R$ {:.2f}".format(adicional_limpeza()))
