# Exercício 1: Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

valor=int(input("Digite um numero para verificar se é positivo ou negativo: "))

if valor >0:
    print("O valor é positivo!")
elif valor<0:
    print("O valor é negativo!")
else:
    print("O valor é zero")

#Exercício 2: Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B.
#Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.

A= int(input("Digite o valor de A: "))
B= int(input("Digite o valor de B: "))
if B==0:
    print("O valor de B nao pode ser zero!")
else:
    print("O valor de A dividido por B é",A/B)

#Exercício 3: Crie um programa que recebe um valor inteiro referente a um determinado ano.
#Imprima na tela se o ano informado é bissexto ou não (para simplificar, você pode utilizar apenas a informação de o ano é divisível por 4 ou não).

ano = int(input("Digite o ano que deseja verificar se é bissexto: "))

if ano %4==0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")

#Exercício 4: Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário
#ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, sendo o GA valendo 30% e o GB valendo 70%).
#Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.

GA=float(input("Digite a nota do Grau A:"))
GB=float(input("Digite a nota do Grau B:"))

if GA <0 or GB<0:
    notafinal = 0.3*GA + 0.7*GB
    if notafinal >= 6:
        print("Voce esta aprovado, sua nota foi de:", notafinal)
    else:
        print("Precisa fazer o Grau C! Sua nota foi de", notafinal)
else:
    print("A nota não pode ser menor que zero.")

#Exercício 5. Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

letra=input("Digite uma letra para verificar se é vogal ou consoante:")

if letra.lower() in "aeiou":
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")

#-----------------------------------------------------------------------------------------------------------------------

#Q: Exercício 6. O que é um parâmetro de entrada de um metodo?
#A: São valores que o metodo necessita receber para poder realizar sua função. Os
#parâmetros de entrada são definidos dentro dos parêntesis do metodo e
#permitem que o metodo receba informações externas de quem o invocou.



#Q: Exercício 7. O que é o retorno de um metodo?
#A: É o valor que o metodo dará como resposta a quem o invocou após realizar sua
#função. Quando um metodo retorna algum valor, quem invocou o metodo
#receberá este valor e pode utilizá-lo na continuidade do programa

#-----------------------------------------------------------------------------------------------------------------------

#Exercício 8. Utilizando while, crie um programa que imprime os números de 0 a 1000.

n1=0

while n1<=1000:
    print(n1)
    n1 +=1

#Exercício 9. Utilizando while, crie um programa que imprime os números pares de 0 a 2000.
n2=0

while n2<=2000:
    print(n2)
    n2 +=2

#Exercício 10. Utilizando while, crie um programa que imprime os números de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).

n3=1000

while n3>=0:
    print(n3)
    n3 -=1

#Exercício 11. Utilizando while, crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados.

contador=0
soma=0

while contador<10:
    numero1 = int(input("Digite um numero inteiro para somar:"))
    soma += numero1
    contador +=1

print("O valor da soma é de ", soma)

#-----------------------------------------------------------------------------------------------------------------------

#Q:Exercício 12. Comparando os comandos de repetição for e while, em quais ocasiões é mais comum a utilização de um ou de outro?
# O comando while geralmente é mais utilizado quando não sabemos a quantidade
# de repetições que nosso código fará. Por exemplo, “enquanto o usuário não
# acertar o usuário e a senha, peça novamente”. Já o comando for é mais utilizado
# quando sabemos o número de iterações a realizar. Por exemplo, “o usuário possui
# 5 tentativas para acertar o usuário e a senha”
#-----------------------------------------------------------------------------------------------------------------------

#Exercício 13. Utilizando for, crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o 100).

for N in range (1,101):
    print(N)

#Exercício 14. Utilizando for,crie um programa que imprime a tabuada de um número inteiro digitado pelo usuário.

multi = int(input("Digite o numero para ver a tabuada:"))

for m in range (1,11):
    print(f"{multi} x {m} = {multi*m}")

#Exercício 15. Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente, solicite que ele informe quantos produtos serão adicionados na lista.
#Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras do usuário.

quantidade_produtos=int(input("Quantos produtos voce deseja adicionar?"))
lista_produtos=[]

for q in range (quantidade_produtos):
    produto=input(f"Digite o nome do produto {q+1}:")
    lista_produtos.append(produto)

print("\nSua lista de compras é")
for produto in lista_produtos:
    print(produto)
