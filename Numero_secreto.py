import random
numero_secreto = random.randint (1,10)
tentativa=0
contagem_tentativa = 0
print ("Bem-vindo ao jogo Número Secreto ")
print("Tente advinhar o Número Secreto entre 1 ao 10 ")
while tentativa != numero_secreto:
   numero = int(input("Digite um numero: "))
   contagem_tentativa = contagem_tentativa +1 
   if numero == numero_secreto :
       print ("Parabéns ! Você advinhou número secreto") 
       print (f"Você presisou de : {tentativa} tentativas")
       break
   elif numero < numero_secreto :
       print ("O numero secreto é maior.")
   else : 
       print ("O numero secreto é menor")
       