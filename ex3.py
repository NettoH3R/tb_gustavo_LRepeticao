
num = int(input("Digite um numero: "))

if num <= 0 :
    print("Digite um numero positivo")
    
else:
    i = 1
    while i < num :
        if num % i == 0 and i != 1:
            primo = False
            break
        else:
            primo = True
        i += 1


    if primo:
        print("Esse numero é primo")
    else:
        print("Esse numero não é primo")