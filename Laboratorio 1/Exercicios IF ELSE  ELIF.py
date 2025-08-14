# Exercicio 1
valor = int(input("Digite um valor para verificar se é positivo ou negativo:"))

if valor >0:
    print("O valor é positivo!")
elif valor <0:
    print("O valor é negativo!")
else:
    print("O valor é zero!")

#----------------------------------------------------------------------------------------------

#Exercicio 2
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))

if valor1 > valor2:
    print("O primeiro valor é maior que o segundo!")
elif valor1 < valor2:
    print("O segundo valor é maior que o primeiro!")
else:
    print("Os valores são iguais!")

#----------------------------------------------------------------------------------------------

#Exercicio 3
A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))

if B !=0:
    resultado = A/B
    print("O valor da divisão de A por B é:", resultado)
else:
    print("O valor B não pode ser 0, reinicie a operação!")

#----------------------------------------------------------------------------------------------
#Exercicio 4
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

#Exercicio 5
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

#Exercicio 6
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

#Exercicio 7
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

#Exercicio 8
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

#Exercicio 9
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

#Exercicio 10
letra = input("Digite uma letra para saber se é vogal ou consoante:")

if letra.lower() in "aeiou":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")


