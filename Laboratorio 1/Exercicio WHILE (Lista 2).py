# Exercicio 1: Faça o código que implementa o algoritmo descrito no fluxograma abaixo:
contador = 0

while contador <10:
    numero = int(input("Digite um numero para verificar se ele é positivo, negativo ou zero:"))
    if numero <0:
        print("O numero é negativo!")
    elif numero ==0:
        print("O numero é zero!")
    else:
        print("O numero é positivo!")
    contador +=1

# Exercício 2. Faça um programa que escreva na tela todos os números inteiros entre 0 (inclusive) e 1000 (inclusive).

contador = 0

while contador <=1000:
    print(contador)
    contador+=1

# Exercício 3. Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digitados pelo usuário (num1 e num2).
# Caso num1 seja maior do que num2, imprima uma mensagem de erro e não imprima.

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

if num1 > num2:
    print("O primeiro valor nao pode ser maior que o segundo valor!")
else:
    contador = num1
    while contador <= num2:
        print(contador)
        contador +=1

# Exercício 4. Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário (num1 e num2). Caso
# num1 seja maior do que num2, seu programa deve imprimir os valores entre num1 e num2 da mesma forma.

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

if num1 < num2:
    contador = num1
    while contador <=num2:
        print(contador)
        contador+=1
else:
    contador = num1
    while contador >=num2:
        print(contador)
        contador-=1

# Exercício 5. Faça um programa que imprima na tela a soma de todos os valores entre 1 e 1000.

soma = 0
for n in range (0,1001):
    soma+=n
print("A soma de 1 até 1000 é de",soma)

# Exercício 6. Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando o usuário digitar um
# número que não seja o solicitado, imprima na tela a soma dos valores positivos e pares digitados.

soma = 0

while True:
    numero = int(input("Digite um numero positivo e par:"))
    if numero <0 or numero%2==1:
        print("O numero nao pode ser negativo e nem impar!")
        break
    soma += numero
print("A soma dos numeros positivos e pares digitados é",soma)

# Exercício 7. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele digite
# seu usuário e senha. O programa só termina quando ele acertar o usuário e a senha. Quando ele acertar, você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO.

login_usuario="USER10"
senha_usuario="PASSWORD1234"

while True:
    input_login = input("Digite o login:")
    input_senha = input("Digite a senha:")

    if input_login !=login_usuario or input_senha!=senha_usuario:
        print("Senha ou Login errados, tente novamente")
    else:
        print("Login efetuado com sucesso")
        break

# Exercício 8. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele
# digite seu usuário e senha. O programa termina quando ele acertar o usuário e a senha ou quando ele exceder o máximo de 3 tentativas. Quando ele acertar, o programa deve
# informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas, o programa deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!

tentativas = 0
login_usuario="USER10"
senha_usuario="PASSWORD1234"

while tentativas <3:
    input_login = input("Digite o login:")
    input_senha = input("Digite a senha:")

    if input_login ==login_usuario and input_senha==senha_usuario:
        print("Login efetuado com sucesso")
        break
    else:
        tentativas+=1
        print("Senha ou login incorreto, tente novamente:")

        if tentativas ==3:
            print("Limite maximo de tentativas excedido!")