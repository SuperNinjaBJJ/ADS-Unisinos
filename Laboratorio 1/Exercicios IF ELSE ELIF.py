# Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.
valor = int(input("Digite um valor para verificar se é positivo ou negativo:"))  # lê um valor inteiro do usuário

if valor > 0:  # verifica se o valor é positivo
    print("O valor é positivo!")  # imprime positivo
elif valor < 0:  # verifica se o valor é negativo
    print("O valor é negativo!")  # imprime negativo
else:  # se não for positivo nem negativo
    print("O valor é zero!")  # imprime zero

#----------------------------------------------------------------------------------------------

#Exercício 2. Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.
valor1 = int(input("Digite o primeiro valor:"))  # lê o primeiro valor
valor2 = int(input("Digite o segundo valor:"))  # lê o segundo valor

if valor1 > valor2:  # verifica se o primeiro valor é maior
    print("O primeiro valor é maior que o segundo!")  # imprime resultado
elif valor1 < valor2:  # verifica se o segundo valor é maior
    print("O segundo valor é maior que o primeiro!")  # imprime resultado
else:  # se nenhum for maior
    print("Os valores são iguais!")  # imprime igualdade

#----------------------------------------------------------------------------------------------

#Exercício 3. Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B.
# Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.
A = int(input("Digite o valor de A:"))  # lê o valor A
B = int(input("Digite o valor de B:"))  # lê o valor B

if B != 0:  # verifica se B não é zero
    resultado = A / B  # realiza a divisão
    print("O valor da divisão de A por B é:", resultado)  # imprime resultado
else:  # se B for zero
    print("O valor B não pode ser 0, reinicie a operação!")  # mensagem de erro

#----------------------------------------------------------------------------------------------
#Exercício 4. Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.
int1 = int(input("Digite o primeiro valor:"))  # lê primeiro valor
int2 = int(input("Digite o segundo valor:"))  # lê segundo valor
int3 = int(input("Digite o terceiro valor:"))  # lê terceiro valor

if int1 < int2 and int1 < int3:  # verifica se o primeiro é menor que os outros dois
    print("O primeiro valor é o menor")  # imprime resultado
elif int2 < int3 and int2 < int1:  # verifica se o segundo é menor
    print("O segundo valor é o menor")  # imprime resultado
elif int3 < int2 and int3 < int1:  # verifica se o terceiro é menor
    print("O terceiro valor é o menor")  # imprime resultado
else:  # se todos forem iguais ou zeros
    print("O valor de todos é zero.")  # imprime resultado

#----------------------------------------------------------------------------------------------

#Exercício 5. Crie um programa que recebe o preço de um produto pelo teclado e imprime mensagem adequada.
preco = float(input("Digite o preço do produto ou serviço:"))  # lê o preço do produto

if preco <= 0:  # verifica se o preço é zero ou negativo
    print("O preço nao pode ser negativo nem zero.")  # imprime aviso
elif preco > 0 and preco <= 30:  # verifica se é baixo
    print("O preço do produto/serviço é baixo!")  # imprime categoria
elif preco > 30 and preco <= 50:  # verifica se é médio
    print("O preço do produto/serviço é médio!")  # imprime categoria
else:  # se for maior que 50
    print("O preço do produto/serviço é alto.")  # imprime categoria

#----------------------------------------------------------------------------------------------

#Exercício 6. Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado.
jur = int(input("Digite o preço do produto:"))  # lê preço do produto

if jur != 0 and jur < 100:  # verifica faixa de preço menor que 100
    jur10 = ((jur * 0.1) + jur)  # aplica 10% de juros
    print("O novo preço corrigido com 10% de juros é de: ", jur10)  # imprime resultado
elif jur >= 100 and jur <= 300:  # verifica faixa entre 100 e 300
    jur20 = ((jur * 0.2) + jur)  # aplica 20% de juros
    print("O novo preço corrigido com 20% de juros é de:", jur20)  # imprime resultado
elif jur >= 300 and jur <= 1000:  # verifica faixa entre 300 e 1000
    jur50 = ((jur * 0.5) + jur)  # aplica 50% de juros
    print("O novo preço corrigido com 50% de juros é de:", jur50)  # imprime resultado
else:  # se for zero ou inválido
    print("O preço nao pode ser zero")  # imprime aviso

#Exercício 7. Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima se é bissexto.
ano = int(input("Digite um ano(Ex: 2025):"))  # lê o ano

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):  # verifica se é bissexto
    bissexto = True  # define como bissexto
else:
    bissexto = False  # define como não bissexto

if bissexto:  # se for bissexto
    print("O ano é bissexto!")  # imprime mensagem
else:
    print("O ano não é bissexto!")  # imprime mensagem

#----------------------------------------------------------------------------------------------

#Exercício 8. Crie um programa que exibe um menu de calculadora na tela.
print("Selecione a opção desejada na lista abaixo")  # imprime menu
print("Digite 1 para soma")  # opção 1
print("Digite 2 para subtração")  # opção 2
print("Digite 3 para multiplicar")  # opção 3
print("Digite 4 para dividir")  # opção 4
print("Digite 5 para potencia")  # opção 5
print("Digite 6 para radiciação")  # opção 6
print("Digite qualquer outro numero para sair")  # opção padrão
opcao = int(input("Digite sua opção:"))  # lê opção do usuário

if opcao == 1:  # se opção soma
    soma1 = float(input("Digite o primeiro valor: "))  # lê primeiro valor
    soma2 = float(input("Digite o segundo valor: "))  # lê segundo valor
    resultado1 = soma1 + soma2  # calcula soma
    print("O resultado é: ", resultado1)  # imprime resultado
elif opcao == 2:  # se opção subtração
    sub1 = float(input("Digite o primeiro valor: "))  # lê primeiro valor
    sub2 = float(input("Digite o segundo valor: "))  # lê segundo valor
    resultado2 = sub1 - sub2  # calcula subtração
    print("O resultado é: ", resultado2)  # imprime resultado
elif opcao == 3:  # se opção multiplicação
    mult1 = float(input("Digite o primeiro valor: "))  # lê primeiro valor
    mult2 = float(input("Digite o segundo valor: "))  # lê segundo valor
    resultado3 = mult1 * mult2  # calcula multiplicação
    print("O resultado é: ", resultado3)  # imprime resultado
elif opcao == 4:  # se opção divisão
    div1 = float(input("Digite o primeiro valor: "))  # lê primeiro valor
    div2 = float(input("Digite o segundo valor: "))  # lê segundo valor
    resultado4 = div1 / div2  # calcula divisão
    print("O resultado é: ", resultado4)  # imprime resultado
elif opcao == 5:  # se opção potência
    pot1 = float(input("Digite o valor da base: "))  # lê base
    pot2 = float(input("Digite o valor do expoente: "))  # lê expoente
    resultado5 = pot1 ** pot2  # calcula potência
    print("O resultado é: ", resultado5)  # imprime resultado
elif opcao == 6:  # se opção radiciação
    rad1 = float(input("Digite o valor do radicando: "))  # lê radicando
    rad2 = float(input("Digite o valor do indice: "))  # lê índice
    resultado6 = rad1 ** (1 / rad2)  # calcula raiz
    print("O resultado é: ", resultado6)  # imprime resultado
else:  # qualquer outra opção
    print("Saindo...")  # imprime mensagem de saída

#----------------------------------------------------------------------------------------------

#Exercício 9. Crie um programa que recebe a nota do Grau A e Grau B e informa se será necessário Grau C.
grauA = float(input("Digite sua nota total do Grau A: "))  # lê nota do Grau A
grauB = float(input("Digite sua nota total do Grau B: "))  # lê nota do Grau B

if grauA >= 0 and grauB >= 0:  # verifica se notas são válidas
    notaFinal = 0.33 * grauA + 0.67 * grauB  # calcula nota ponderada
    if notaFinal >= 6:  # verifica se passou
        print("Não precisa de Grau C")  # imprime resultado
    else:  # se não passou
        print("Precisa de Grau C")  # imprime resultado
else:  # se alguma nota for negativa
    print("A nota não pode ser negativa.")  # imprime aviso

#----------------------------------------------------------------------------------------------

#Exercício 10. Crie um programa que solicita que o usuário digite uma letra e imprime se é vogal ou consoante.
letra = input("Digite uma letra para saber se é vogal ou consoante:")  # lê a letra

if letra.lower() in "aeiou":  # verifica se é vogal
    print("A letra é uma vogal.")  # imprime resultado
else:  # se não for vogal
    print("A letra é uma consoante.")  # imprime resultado
