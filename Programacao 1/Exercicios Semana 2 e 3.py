# Exercício 1: Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

valor = int(input("Digite um numero para verificar se é positivo ou negativo: "))  # lê um valor inteiro do usuário

if valor > 0:  # verifica se o valor é positivo
    print("O valor é positivo!")  # imprime positivo
elif valor < 0:  # verifica se o valor é negativo
    print("O valor é negativo!")  # imprime negativo
else:  # se não for positivo nem negativo
    print("O valor é zero")  # imprime zero

# Exercício 2: Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B.
# Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.

A = int(input("Digite o valor de A: "))  # lê o valor A
B = int(input("Digite o valor de B: "))  # lê o valor B

if B == 0:  # verifica se B é zero
    print("O valor de B nao pode ser zero!")  # imprime mensagem de erro
else:  # se B não for zero
    print("O valor de A dividido por B é", A / B)  # realiza a divisão e imprime

# Exercício 3: Crie um programa que recebe um valor inteiro referente a um determinado ano.
# Imprima na tela se o ano informado é bissexto ou não.

ano = int(input("Digite o ano que deseja verificar se é bissexto: "))  # lê o ano

if ano % 4 == 0:  # verifica se é divisível por 4
    print("O ano é bissexto!")  # imprime se for bissexto
else:  # se não for divisível por 4
    print("O ano não é bissexto!")  # imprime se não for bissexto

# Exercício 4: Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime se será necessário realizar o Grau C.

GA = float(input("Digite a nota do Grau A: "))  # lê nota do Grau A
GB = float(input("Digite a nota do Grau B: "))  # lê nota do Grau B

if GA < 0 or GB < 0:  # verifica se alguma nota é negativa
    print("A nota não pode ser menor que zero.")  # mensagem de erro
else:  # se ambas forem válidas
    notafinal = 0.3 * GA + 0.7 * GB  # calcula nota ponderada
    if notafinal >= 6:  # verifica aprovação
        print("Voce esta aprovado, sua nota foi de:", notafinal)  # imprime aprovação
    else:  # se não atingiu nota mínima
        print("Precisa fazer o Grau C! Sua nota foi de", notafinal)  # imprime necessidade do Grau C

# Exercício 5: Crie um programa que solicita que o usuário digite uma letra e imprime se é vogal ou consoante.

letra = input("Digite uma letra para verificar se é vogal ou consoante: ")  # lê a letra

if letra.lower() in "aeiou":  # verifica se é vogal
    print("A letra digitada é uma vogal.")  # imprime vogal
else:  # se não for vogal
    print("A letra digitada é uma consoante.")  # imprime consoante

# Exercício 6: O que é um parâmetro de entrada de um método?
# São valores que o método precisa receber para realizar sua função.

# Exercício 7: O que é o retorno de um método?
# É o valor que o método fornece após executar sua função para quem o invocou.

# Exercício 8: Utilizando while, crie um programa que imprime os números de 0 a 1000.

n1 = 0  # inicializa contador
while n1 <= 1000:  # enquanto for menor ou igual a 1000
    print(n1)  # imprime número atual
    n1 += 1  # incrementa contador

# Exercício 9: Utilizando while, crie um programa que imprime os números pares de 0 a 2000.

n2 = 0  # inicializa contador
while n2 <= 2000:  # enquanto for menor ou igual a 2000
    print(n2)  # imprime número atual
    n2 += 2  # incrementa de 2 em 2 para pegar pares

# Exercício 10: Utilizando while, crie um programa que imprime os números de 0 a 1000 em ordem decrescente.

n3 = 1000  # inicializa contador no maior valor
while n3 >= 0:  # enquanto for maior ou igual a 0
    print(n3)  # imprime número atual
    n3 -= 1  # decrementa contador

# Exercício 11: Utilizando while, crie um programa que solicita 10 valores inteiros e imprime a soma.

contador = 0  # inicializa contador
soma = 0  # inicializa soma

while contador < 10:  # enquanto não tiver digitado 10 números
    numero1 = int(input("Digite um numero inteiro para somar: "))  # lê número
    soma += numero1  # adiciona à soma
    contador += 1  # incrementa contador

print("O valor da soma é de", soma)  # imprime resultado final

# Exercício 12: Comparando for e while.
# while é usado quando não sabemos o número de repetições.
# for é usado quando sabemos o número exato de iterações.

# Exercício 13: Utilizando for, imprima os valores de 1 a 100.

for N in range(1, 101):  # percorre de 1 a 100
    print(N)  # imprime cada número

# Exercício 14: Utilizando for, imprima a tabuada de um número inteiro digitado pelo usuário.

multi = int(input("Digite o numero para ver a tabuada: "))  # lê o número
for m in range(1, 11):  # percorre de 1 a 10
    print(f"{multi} x {m} = {multi * m}")  # imprime multiplicação

# Exercício 15: Crie um programa que permita ao usuário criar sua lista de compras.

quantidade_produtos = int(input("Quantos produtos voce deseja adicionar? "))  # lê quantidade
lista_produtos = []  # inicializa lista vazia

for q in range(quantidade_produtos):  # para cada produto
    produto = input(f"Digite o nome do produto {q+1}: ")  # lê produto
    lista_produtos.append(produto)  # adiciona à lista

print("\nSua lista de compras é")
for produto in lista_produtos:  # percorre lista
    print(produto)  # imprime cada produto
