nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite a sua altura: "))
print("Sua idade é: ", idade)
print("Seu nome é: ", nome)
print("Sua altura é: ", altura)
print("Obrigado!")

#----------------------------------------------------------------------------------------------

# Pedir informações ao usuario
nome = input("Qual seu nome? ")
nomeRua = input("Agora me fala, qual o nome da sua rua? ")
numeroCasa = int(input("E qual o numero da sua casa? "))
cep = input("Certo, qual o seu CEP? ")
bairro = input("Ultima pergunta, qual o nome do seu bairro? ")

# Imprimir na tela
print("Nome do usuario: " , nome)
print("Endereço:" , nomeRua, numeroCasa)
print("CEP:" , cep)
print("Bairro:" , bairro)

#----------------------------------------------------------------------------------------------

# Solicitar valores
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))
numero4 = int(input("Digite o quarto valor: "))
numero5 = int(input("Digite o quinto valor: "))

# Resultado da Soma
soma = numero1 + numero2 + numero3 + numero4 + numero5
print("O valor da soma de todos os numeros é: ", soma)

# Resultado do Produto
produto = numero1 * numero2 * numero3 * numero4 * numero5
print("O valor do produto de todos os numeros é: ", produto)

#----------------------------------------------------------------------------------------------

A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
D = int(input("Digite o quarto valor: "))
E = int(input("Digite o quinto valor: "))

# Area do Triangulo
areaTriangulo = B*C/2
print("A area do triângulo é: ", areaTriangulo)

# Perimetro do Retangulo
perimetroRetangulo = 2*(A+B+C+D)
print("O perimetro do retangulo é: ", perimetroRetangulo)

# Area do Circulo
areaCirculo = 3.14*(E**2)
print("A area do circulo é: ",areaCirculo)

#----------------------------------------------------------------------------------------------

trabalho = float(input("Digite a sua nota no trabalho: "))
prova = float(input("Digite a sua nota na prova: "))
teste = float(input("Digite a sua nota no teste: "))
notaFinal= (0.1*trabalho)+(0.6*prova)+(0.3*teste)
print("Sua nota final foi de ",notaFinal)3

#----------------------------------------------------------------------------------------------

atvPratica = float(input("Qual a sua nota na atividade prática do Grau A?"))*0.45
atvTeorica = float(input("Qual a sua nota na atividade teórica do Grau A?"))*0.55
provaLab = float(input("Qual a sua nota na prova em laboratório? "))*0.6
testeTeorico = float(input("Qual a sua nota no teste teórico? "))*0.2
trabalhoEx = float(input("Qual a sua nota no trabalho extraclasse? "))*0.2
grauA = atvPratica+atvTeorica*0.33
grauB = provaLab+testeTeorico+trabalhoEx*0.67
grauAB = grauA+grauB

print("Sua nota final no Grau A foi: ",grauA)
print("Sua nota final no Grau B foi: ",grauB)
print("Sua nota final foi de: ",grauAB)