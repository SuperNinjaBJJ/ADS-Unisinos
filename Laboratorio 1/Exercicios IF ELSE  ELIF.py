# Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.
valor = int(input("Digite um valor para verificar se é positivo ou negativo:"))

if valor >0:
    print("O valor é positivo!")
elif valor <0:
    print("O valor é negativo!")
else:
    print("O valor é zero!")

#----------------------------------------------------------------------------------------------

#Exercício 2. Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.

valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))

if valor1 > valor2:
    print("O primeiro valor é maior que o segundo!")
elif valor1 < valor2:
    print("O segundo valor é maior que o primeiro!")
else:
    print("Os valores são iguais!")

#----------------------------------------------------------------------------------------------

#Exercício 3. Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B.
# Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.
A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))

if B !=0:
    resultado = A/B
    print("O valor da divisão de A por B é:", resultado)
else:
    print("O valor B não pode ser 0, reinicie a operação!")

#----------------------------------------------------------------------------------------------
#Exercício 4. Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.
int1 = int(input("Digite o primeiro valor:"))
int2 = int(input("Digite o segundo valor:"))
int3 = int(input("Digite o terceiro valor:"))

if int1 < int2 and int1 < int3:
    print("O primeiro valor é o menor")
elif int2 < int3 and int2 < int1:
    print("O segundo valor é o menor")
elif int3 < int2 and int3 < int1:
    print("o terceiro valor é o menor")
else:
    print("O valor de todos é zero.")

#----------------------------------------------------------------------------------------------

#Exercício 5. Crie um programa que recebe o preço de um produto pelo teclado e imprime na tela a mensagem adequada, de acordo com o preço:

preco = float(input("Digite o preço do produto ou serviço:"))

if preco <=0:
    print("O preço nao pode ser negativo nem zero.")
elif preco >=0 and preco<=30:
    print("O preço do produto/serviço é baixo!")
elif preco >=30 and preco<=50:
    print("O preço do produto/serviço é médio!")
else:
    print("O preço do produto/serviço é alto.")

#----------------------------------------------------------------------------------------------

#Exercício 6. Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa aplicada deve ser:
jur = int(input("Digite o preço do produto:"))

if jur !=0 and jur < 100:
    jur10 =  ((jur*0.1)+jur)
    print("O novo preço corrigido com 10% de juros é de: ", jur10)
elif jur >=100 and jur<=300:
    jur20 = ((jur * 0.2) + jur)
    print("O novo preço corrigido com 20% de juros é de:", jur20)
elif jur >=300 and jur<=1000:
    jur50 = ((jur * 0.5) + jur)
    print("O novo preço corrigido com 50% de juros é de:", jur50)
else:
    print("O preço nao pode ser zero")

#Exercício 7. Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não.
ano = int(input("Digite um ano(Ex: 2025):"))

if (ano % 400 ==0) or (ano % 4==0 and ano % 100!=0):
    bissexto = True
else:
    bissexto = False

if bissexto:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")

#----------------------------------------------------------------------------------------------

#Exercício 8. Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:

print("Selecione a opção desejada na lista abaixo")
print("Digite 1 para soma")
print("Digite 2 para subtração")
print("Digite 3 para multiplicar")
print("Digite 4 para dividir")
print("Digite 5 para potencia")
print("Digite 6 para radiciação")
print("Digite qualquer outro numero para sair")
opcao = int(input("Digite sua opção:"))

if opcao ==1:
    soma1 = float(input("Digite o primeiro valor: "))
    soma2 = float(input("Digite o segundo valor: "))
    resultado1 = soma1+soma2
    print("O resultado é: ", resultado1)
elif opcao==2:
    sub1 = float(input("Digite o primeiro valor: "))
    sub2 = float(input("Digite o segundo valor: "))
    resultado2 = sub1-sub2
    print("O resultado é: ", resultado2)
elif opcao==3:
    mult1 = float(input("Digite o primeiro valor: "))
    mult2 = float(input("Digite o segundo valor: "))
    resultado3 = mult1*mult2
    print("O resultado é: ", resultado3)
elif opcao==4:
    div1 = float(input("Digite o primeiro valor: "))
    div2 = float(input("Digite o segundo valor: "))
    resultado4 = div1/div2
    print("O resultado é: ", resultado4)
elif opcao==5:
    pot1 = float(input("Digite o valor da base: "))
    pot2 = float(input("Digite o valor do expoente: "))
    resultado5 = pot1**pot2
    print("O resultado é: ", resultado5)
elif opcao==6:
    rad1 = float(input("Digite o valor do radicando: "))
    rad2 = float(input("Digite o valor do indice: "))
    resultado6 = rad1**(1/rad2)
    print("O resultado é: ", resultado6)
else:
    print("Saindo...")

#----------------------------------------------------------------------------------------------

#Exercício 9. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo
#teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o
#sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe
#uma mensagem de erro e não realize o cálculo.
grauA = float(input("Digite sua nota total do Grau A: "))
grauB = float(input("Digite sua nota total do Grau B: "))

if grauA >=0 and grauB >=0:
    notaFinal= 0.33*grauA + 0.67*grauB
    if notaFinal >=6:
        print("Não precisa de Grau C")
    else:
        print("Precisa de Grau C")
else:
    print("A nota não pode ser negativa.")

#----------------------------------------------------------------------------------------------

#Exercício 10. Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.
letra = input("Digite uma letra para saber se é vogal ou consoante:")

if letra.lower() in "aeiou":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")


