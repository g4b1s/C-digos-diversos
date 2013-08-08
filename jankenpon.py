import random 

jogador="" 

while (jogador != "pedra" and jogador != "papel" and jogador != "tesoura"):
	jogador=raw_input("Pedra, Papel ou Tesoura?: ") 
	jogador=jogador.lower() 

dicionario=["pedra","papel","tesoura"] 

computador=random.randint(1,3) 

def resultado(jogador,computador): 
	if jogador=="pedra" and computador==1:
		return "Empatou"
	if jogador=="pedra" and computador==2:
		return "Perdeu"
	if jogador=="pedra" and computador==3:
		return "Ganhou"

	if jogador=="papel" and computador==1:
		return "Ganhou"
	if jogador=="papel" and computador==2:
		return "Empatou"
	if jogador=="papel" and computador==3:
		return "Perdeu"
			
	if jogador=="tesoura" and computador==1:
		return "Perdeu"
	if jogador=="tesoura" and computador==2:
		return "Ganhou"
	if jogador=="tesoura" and computador==3:
		return "Empatou"
print "\nJogador:\t", jogador
print "Computador:\t", dicionario[computador-1] 
print "\n"
print resultado(jogador,computador) 
