print("*********************************")
print ("Bem vindo no jogo de adivinhação!")
print ("*********************************")

numero_secreto = 63

chute = input ("Digite o seu numero: ")

print ("Você digitou", chute)
comparacao = numero_secreto == int (chute)
print ("o valor da comparação é:", comparacao)
if (comparacao) : 
    print ("você acertou!")
else :
    print ("você errou!")
print ("Fim do jogo!")


