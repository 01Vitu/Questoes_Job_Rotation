#Recebe um número do usuário.
num = int(input("Informe um número: "))

#Inicializa as variáveis que representam os dois primeiros valores da sequência de Fibonacci.
num1 = 0
num2 = 1

#Inicializa a variável que indicará se o número pertence ou não à sequência.
pertence = False

#Verifica se o número é igual a um dos dois primeiros valores da sequência.
if num == num1 or num == num2:
    pertence = True

#Caso contrário, calcula os valores da sequência de Fibonacci até que o próximo valor seja maior que o número informado.
else:
    while num2 < num:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if num == num2:
            pertence = True

#Exibe a mensagem indicando se o número pertence ou não à sequência.
if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
