#Define a string.
string = 'onibus'

#Cria uma nova string vazia.
string_invertida = ''

#Percorre a string de trás para frente e adiciona cada caractere na nova string.
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

#Imprime a nova string.
print(string_invertida)
