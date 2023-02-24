from random import randint
print ('=-' * 20)
print ('Jogo de Adivinhação')
print ('=-' * 20)
pc = randint (1,10)
user = 0 #variavel iniciada fora do laço
tentativas = 1
vidas_user = 3 # vidas do jogador

while not user == pc:
  if vidas_user == 0:
    print (f'Game Over!! {vidas_user} vida(s)')
    break
  user = int (input('Digite um número: '))
  print ('=-' * 10)
  if user < pc:
    print (f'Errou, o número é MAIOR que {user}.')
    tentativas += 1
    vidas_user -= 1
    print(f'Você tem mais {vidas_user} vida(s)')
  elif user > pc:
    print (f'Errou, o número é MENOR que {user}.')
    tentativas += 1
    vidas_user -= 1
    print(f'Você tem mais {vidas_user} vida(s)')
  elif user == pc: #usei elif para ficar mais fácil de entender#
    print ('Acertou.. Parabéns')
    print (f'Acertou com {tentativas} tentativas')
    break
  
 