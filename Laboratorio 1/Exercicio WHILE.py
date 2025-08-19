#Exercício 1. Crie um programa que pede para o usuário digitar o nome de 13 pessoas pelo teclado.

nomes_pessoas = 0  # contador de nomes digitados
while nomes_pessoas < 13:  # enquanto não tiver digitado 13 nomes
    print(input("Digite o nome de uma pessoa: "))  # lê e imprime o nome digitado
    nomes_pessoas += 1  # incrementa o contador

#Exercício 2. Crie um programa que imprime os números de 0 a 1000.

numero_1000 = 0  # inicializa o contador
while numero_1000 <= 1000:  # enquanto for menor ou igual a 1000
    print(numero_1000)  # imprime o número atual
    numero_1000 += 1  # incrementa o número em 1

#Exercício 3. Crie um programa que imprime os números pares de 0 a 2000.

numero_2000 = 0  # inicializa contador no primeiro número par
while numero_2000 <= 2000:  # enquanto for menor ou igual a 2000
    print(numero_2000)  # imprime o número atual
    numero_2000 += 2  # incrementa de 2 em 2 para pegar apenas os pares

#Exercício 4. Crie um programa que imprime os números de 0 a 1000 em ordem decrescente.

numero_dec_1000 = 2000  # inicializa contador no maior valor
while numero_dec_1000 >= 0:  # enquanto for maior ou igual a 0
    print(numero_dec_1000)  # imprime o número atual
    numero_dec_1000 -= 1  # decrementa em 1

#Exercício 5. Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final, imprima quantos torcedores torcem para o Grêmio.

torcedores = 0  # contador de entradas de usuários
times = []  # lista para armazenar os times
while torcedores < 3:  # enquanto não tiver 3 entradas
    time = input("Digite o seu time: ").lower()  # lê e transforma em minúsculas
    times.append(time)  # adiciona o time à lista
    torcedores += 1  # incrementa contador
torcedores_gremio = times.count("gremio") + times.count("grêmio")  # conta torcedores do Grêmio
print("O numero de torcedores do Grêmio é:", torcedores_gremio)  # imprime resultado

#Exercício 6. Crie um programa que pede para o usuário digitar 20 números com ponto flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final, imprima a string.

cont_numeros = 0  # contador de números digitados
numeros_flutuantes = []  # lista para armazenar floats
while cont_numeros < 20:  # enquanto não tiver 20 números
    numero = input("Digite um numero qualquer com virgula: ")  # lê input
    numero = numero.replace(",", ".")  # substitui vírgula por ponto
    numero = float(numero)  # converte para float
    numeros_flutuantes.append(numero)  # adiciona à lista
    cont_numeros += 1  # incrementa contador
resultado = sum(numeros_flutuantes)  # soma todos os números da lista
print("A soma de todos é:", resultado)  # imprime soma

#Exercício 7. Crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados.

contador = 0  # contador de entradas
input_usuario = []  # lista para armazenar os números
while contador < 2:  # enquanto não tiver 2 números
    numero = int(input("Digite um valor para somar: "))  # lê e converte para inteiro
    input_usuario.append(numero)  # adiciona à lista
    contador += 1  # incrementa contador
resultado = sum(input_usuario)  # soma todos os números da lista
print("O resultado da soma dos valores é:", resultado)  # imprime soma

#Exercício 8. Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros, e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.

quant = int(input("Quantos numeros voce quer conferir se é positivo ou negativo? "))  # lê a quantidade de números
for q in range(quant):  # repete exatamente quant vezes
    numero = int(input(f"Digite o numero {q+1}: "))  # lê cada número
    if numero < 0:  # verifica se é negativo
        print("O numero é negativo!")  # imprime negativo
    elif numero > 0:  # verifica se é positivo
        print("O numero é positivo")  # imprime positivo
    else:  # se não for positivo nem negativo
        print("O numero é zero!")  # imprime zero

#Exercício 9. Crie um programa que pede para o usuário digitar 2 valores inteiros via Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números pares entre o menor e o maior valor.

val1 = int(input("Digite o primeiro valor: "))  # lê o primeiro valor
val2 = int(input("Digite o segundo valor: "))  # lê o segundo valor
if val1 >= 0 and val2 >= 0:  # verifica se ambos são não-negativos
    menor = min(val1, val2)  # identifica o menor valor
    maior = max(val1, val2)  # identifica o maior valor
    for numero in range(menor, maior + 1):  # percorre todos os números entre menor e maior
        if numero % 2 == 0:  # verifica se o número é par
            print("Os numeros pares entre eles são:", numero)  # imprime número par

#Exercício 10. Crie um programa que faça a soma dos valores de 0 até 198.

soma = 0  # inicializa soma
for numero in range(0, 199):  # percorre todos os números de 0 até 198
    soma += numero  # adiciona cada número à soma
print("A soma de 0 até 198 é", soma)  # imprime resultado

#Exercício 11. Crie um programa que imprima a soma dos valores pares e a soma dos valores ímpares entre dois números quaisquer digitados pelo usuário.

numero_inicial = int(input("Digite o primeiro número: "))# 1. Pede o primeiro número ao usuário
numero_final = int(input("Digite o segundo número: "))# 1. Pede o segundo número ao usuário

soma_pares = 0 # 2. Cria a primeira variável para armazenar a soma dos pares
soma_impares = 0# 2. Cria a segunda variável para armazenar a soma dos ímpares

for n in range(numero_inicial, numero_final + 1):# 3. Percorrer todos os números entre numero_inicial e numero_final
    if n % 2 == 0: # 4. Verificar se o número é par ou ímpar
        soma_pares += n # 5. Adicionar à soma dos pares
    else:
        soma_impares += n # 6. Adicionar à soma dos ímpares

print("Soma dos pares:", soma_pares)# 7. Mostrar os resultados
print("Soma dos ímpares:", soma_impares)# 7. Mostrar os resultados