import json

#Lendo os dados do arquivo json.
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Inicializando as variáveis.
menor_valor = float('inf')
maior_valor = 0
total_dias = 0
soma_valores = 0

#Iterando sobre os dados.
for dia in dados:
    valor = dia['valor']
    #Verificando se o dia teve faturamento.
    if valor > 0:
        #Verificando se o valor é o menor ou maior até o momento.
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor
        #Incrementando a soma dos valores para cálculo da média.
        soma_valores += valor
        total_dias += 1

#Calculando a média dos valores.
media = soma_valores / total_dias

#Contando os dias com faturamento superior à média.
dias_acima_media = sum(dia['valor'] > media for dia in dados)

#Imprimindo os resultados.
print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Dias acima da média: {dias_acima_media}")
