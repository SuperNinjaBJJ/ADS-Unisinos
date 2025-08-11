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