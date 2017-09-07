#!/usr/bin/python 2.7.10
# coding: utf-8

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        #                                                                   #
        #                   MESTRADO EM CIENCIAS DA COMPUTACAO              #
        #           DISCIPLINA DE COMPUTACAO INSPIRADA PELA NATUREZA        #
        #                   Thiago Giroto Milani    -   01/2017             #
        #                                                                   #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#Biblioteca

import random

class Particle:

    V_MAX = 10
    C1 = 2
    C2 = 2
    
    # Chamado qunado um novo objeto de particola e instanciado
    def __init__(self, low, high, target):
        self.low = low
        self.high = high
        self.target = target
        
        # Seta os valor dos atributos A, B, C, e D    
        self.A = 1
        self.B = -5
        self.C = 100
        self.D = 5
        # Aplica valores inicias aos atributos do algoritmo do PSO
        self.pBest = abs(((self.A-(self.B))**2+self.C*(self.D-(self.B**2))**2) - self.target)
        self.velocity = 0
        self.fitness = self.pBest
            
    # Atualizar o valor de aptidao para esta particula e verifica se seu melhor esta em pBest
    def calculateFitness(self):
        # Calculate the distance from the TARGET value
        self.fitness = abs(((self.A-(self.B))**2+self.C*(self.D-(self.B**2))**2) - self.target)
        if (self.fitness < self.pBest):
            self.pBest = self.fitness

    # Atualiza este atributos de partículas A, B, C, D, com base na equação de Eberhart & Kennedy
    def update(self, gBest):
        # Verifica test = a particola corrente
        test = (self.A-(self.B))**2+self.C*(self.D-(self.B**2))**2
        # Gera alguns numeros aleatorios entre 0 - 1 para a equacao
        R1 = random.random()
        R2 = random.random()

        # E B E R H A R T   &   K E N N E D Y
        self.velocity = self.velocity + Particle.C1 * R1 * (self.pBest - test) + Particle.C2 * R2 * (gBest - test)

        # Controla a velocidade, Para o melhor extravazar
        if (self.velocity > Particle.V_MAX):
            self.velocity = Particle.V_MAX
        elif (self.velocity < -Particle.V_MAX):
            self.velocity = -Particle.V_MAX
        
        # Atualiza os atributos A, B, C, D com a nova velocidade
        self.A = int(self.A + self.velocity)
        #self.B = int(self.B + self.velocity)
        self.C = int(self.C + self.velocity)
        #self.D = int(self.D + self.velocity)
    
    # Define como irá imprimir essa classe de partículas
    def __str__(self):
        total = (self.A-(self.B))**2+self.C*(self.D-(self.B**2))**2
        return "({0} - ({1}))^2 + {2} * ({3} - ({4}^2))^2  = {5}".format(self.A, self.B, self.C, self.D, self.B, total)
        
        
        

    
    
