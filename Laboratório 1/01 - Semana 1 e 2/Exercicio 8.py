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