def mostrar_divisores(numero):

    divisores = []
    count = 0

    for i in range(1, numero+1):

        if numero % i == 0:
            divisores.append(i)
            count += 1

    return divisores, count





def main():

    num = int(input("Digite um numero: "))

    if num <= 0 :
        print("Digite um numero positivo")  
    else:
        print(f"Os divisores são {mostrar_divisores(num)[0]}")
        print(f"Esse numero tem {mostrar_divisores(num)[1] } divisores")