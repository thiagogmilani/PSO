#!/usr/bin/python 2.7.10
# coding: utf-8

		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
		#																	#
		#					MESTRADO EM CIENCIAS DA COMPUTACAO				#
		#			DISCIPLINA DE COMPUTACAO INSPIRADA PELA NATUREZA		#
		#					Thiago Giroto Milani	-	01/2017				#
		#																	#
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#Biblioteca

from particle import Particle

# Definicao de alguns parametros de controle do enxame
MAX_GENERATIONS = 50
NUM_PARTICLES = 10

def main():
	# Manter o controle de melhor solucao global e seu indice dentro do enxame 
    gBest = 100000
    gBestIndex = 0

    # Cria o enxame - criar uma lista de particulas de tamanho NUM_PARTICLES
    swarm = [Particle(0,100,50) for i  in range(NUM_PARTICLES)]
    
    # Definir o contador de loop e a condicao de parada
    generations = 0
    converged = False
    while(generations < MAX_GENERATIONS and (not converged)):
        
        # Calcula os valores de aptidao para o enxame e verificar se temos uma solucao
        for i in range(NUM_PARTICLES):
            swarm[i].calculateFitness()
            converged = converged or (swarm[i].fitness == 0)
              
        # Imprimir as saidas 
        print "[] Generation: " + str(generations)
        for i in range(NUM_PARTICLES):
        	print swarm[i]

        # Seleciona o melhor global baseado no enxame   
        for i in range(NUM_PARTICLES):
            if (swarm[i].pBest < gBest):
                gBest = swarm[i].pBest
                gBestIndex = i
        
        # Atualizar todos mas a particula melhor global usa a equacao de Eberhart & Kennedy       
        for i in range(NUM_PARTICLES):
            if (i != gBestIndex):
                swarm[i].update(gBest)
        
        # Define proxima geracao        
        generations = generations + 1

if __name__ == '__main__':
    main()