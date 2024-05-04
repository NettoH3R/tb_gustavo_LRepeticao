def fatores_primos(numero):
    fatores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
    return fatores




def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo maior que zero.")
    else:
        print("Fatores primos de", numero, "são:", fatores_primos(numero))
