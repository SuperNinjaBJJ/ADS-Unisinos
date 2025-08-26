# Exercicio 1: Faça o código que implementa o algoritmo descrito no fluxograma abaixo:
contador = 0  # Inicializa o contador com 0

while contador < 10:  # Enquanto o contador for menor que 10, repete o loop
    numero = int(input("Digite um numero para verificar se ele é positivo, negativo ou zero:"))  # Solicita ao usuário um número e converte para inteiro
    if numero < 0:  # Se o número for menor que 0
        print("O numero é negativo!")  # Imprime que o número é negativo
    elif numero == 0:  # Se o número for igual a 0
        print("O numero é zero!")  # Imprime que o número é zero
    else:  # Se o número não for menor que 0 nem igual a 0
        print("O numero é positivo!")  # Imprime que o número é positivo
    contador += 1  # Incrementa o contador em 1

# Exercício 2. Faça um programa que escreva na tela todos os números inteiros entre 0 (inclusive) e 1000 (inclusive).
contador = 0  # Inicializa o contador com 0

while contador <= 1000:  # Enquanto o contador for menor ou igual a 1000, repete o loop
    print(contador)  # Imprime o valor atual do contador
    contador += 1  # Incrementa o contador em 1

# Exercício 3. Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digitados pelo usuário (num1 e num2).
# Caso num1 seja maior do que num2, imprima uma mensagem de erro e não imprima.
num1 = int(input("Digite o primeiro valor:"))  # Solicita ao usuário o primeiro número e converte para inteiro
num2 = int(input("Digite o segundo valor:"))  # Solicita ao usuário o segundo número e converte para inteiro

if num1 > num2:  # Se o primeiro número for maior que o segundo
    print("O primeiro valor nao pode ser maior que o segundo valor!")  # Imprime mensagem de erro
else:  # Caso contrário
    contador = num1  # Inicializa o contador com o valor de num1
    while contador <= num2:  # Enquanto o contador for menor ou igual a num2
        print(contador)  # Imprime o valor do contador
        contador += 1  # Incrementa o contador em 1

# Exercício 4. Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário (num1 e num2). Caso
# num1 seja maior do que num2, seu programa deve imprimir os valores entre num1 e num2 da mesma forma.
num1 = int(input("Digite o primeiro valor:"))  # Solicita o primeiro valor
num2 = int(input("Digite o segundo valor:"))  # Solicita o segundo valor

if num1 < num2:  # Se num1 for menor que num2
    contador = num1  # Inicializa contador com num1
    while contador <= num2:  # Enquanto contador for menor ou igual a num2
        print(contador)  # Imprime contador
        contador += 1  # Incrementa contador
else:  # Se num1 for maior ou igual a num2
    contador = num1  # Inicializa contador com num1
    while contador >= num2:  # Enquanto contador for maior ou igual a num2
        print(contador)  # Imprime contador
        contador -= 1  # Decrementa contador

# Exercício 5. Faça um programa que imprima na tela a soma de todos os valores entre 1 e 1000.
soma = 0  # Inicializa a variável soma com 0
for n in range(0, 1001):  # Para cada número de 0 até 1000
    soma += n  # Adiciona o número à soma
print("A soma de 1 até 1000 é de", soma)  # Imprime o resultado da soma

# Exercício 6. Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando o usuário digitar um
# número que não seja o solicitado, imprima na tela a soma dos valores positivos e pares digitados.
soma = 0  # Inicializa soma com 0

while True:  # Loop infinito até encontrar um número inválido
    numero = int(input("Digite um numero positivo e par:"))  # Solicita número ao usuário
    if numero < 0 or numero % 2 == 1:  # Se o número for negativo ou ímpar
        print("O numero nao pode ser negativo e nem impar!")  # Mensagem de erro
        break  # Sai do loop
    soma += numero  # Adiciona número válido à soma
print("A soma dos numeros positivos e pares digitados é", soma)  # Imprime a soma final

# Exercício 7. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele digite
# seu usuário e senha. O programa só termina quando ele acertar o usuário e a senha. Quando ele acertar, você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO.
login_usuario = "USER10"  # Define o login correto
senha_usuario = "PASSWORD1234"  # Define a senha correta

while True:  # Loop infinito até o login correto
    input_login = input("Digite o login:")  # Solicita login ao usuário
    input_senha = input("Digite a senha:")  # Solicita senha ao usuário

    if input_login != login_usuario or input_senha != senha_usuario:  # Se login ou senha estiverem errados
        print("Senha ou Login errados, tente novamente")  # Mensagem de erro
    else:  # Se login e senha estiverem corretos
        print("Login efetuado com sucesso")  # Mensagem de sucesso
        break  # Sai do loop

# Exercício 8. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele
# digite seu usuário e senha. O programa termina quando ele acertar o usuário e a senha ou quando ele exceder o máximo de 3 tentativas. Quando ele acertar, o programa deve
# informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas, o programa deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!
tentativas = 0  # Inicializa contador de tentativas
login_usuario = "USER10"  # Define login correto
senha_usuario = "PASSWORD1234"  # Define senha correta

while tentativas < 3:  # Enquanto o número de tentativas for menor que 3
    input_login = input("Digite o login:")  # Solicita login
    input_senha = input("Digite a senha:")  # Solicita senha

    if input_login == login_usuario and input_senha == senha_usuario:  # Se login e senha estiverem corretos
        print("Login efetuado com sucesso")  # Mensagem de sucesso
        break  # Sai do loop
    else:  # Se login ou senha estiverem incorretos
        tentativas += 1  # Incrementa o contador de tentativas
        print("Senha ou login incorreto, tente novamente:")  # Mensagem de erro
        if tentativas == 3:  # Se atingir 3 tentativas
            print("Limite maximo de tentativas excedido!")  # Mensagem de limite excedido
