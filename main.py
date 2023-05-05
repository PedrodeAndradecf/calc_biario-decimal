def binario_para_decimal(binario):
    decimal = 0
    binario_reverso = str(binario)[::-1]

    for indice, digito in enumerate(binario_reverso):
        if digito == '1':
            decimal += 2**indice
        elif digito != '0':
            raise ValueError(
                "O número informado não é um número binário válido.")

    return decimal


def main():
    continuar = True
    while continuar:
        try:
            binario = input("Digite um número binário: ")
            decimal = binario_para_decimal(binario)
            print(f"O número binário {binario} em decimal é: {decimal}")
        except ValueError as e:
            print(e)

        resposta = ''
        while resposta not in ('s', 'n'):
            resposta = input(
                "Deseja continuar? Digite 's' para sim e 'n' para não: "
            ).lower()
            if resposta not in ('s', 'n'):
                print("Por favor, digite uma resposta válida ('s' ou 'n').")

        if resposta == 'n':
            continuar = False
            print("Fim")


if __name__ == "__main__":
    main()
