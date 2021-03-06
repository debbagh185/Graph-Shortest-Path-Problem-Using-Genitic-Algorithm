#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:55:52 2020

@author: Brahim DEBBAGH
"""

from graph import Graph
from population import Population
from geneticAlgorithm import GA

if __name__ == '__main__':
    
    # Supprimer l'approche orienté objet
    
    g = Graph()

    g.add_vertex(pos=(1,1))
    g.add_vertex(pos=(1,2))
    g.add_vertex(pos=(1,3))
    g.add_vertex(pos=(1,4))
    g.add_vertex(pos=(1,5))
    
    g.add_vertex(pos=(2,1))
    g.add_vertex(pos=(2,2))
    g.add_vertex(pos=(2,3))
    g.add_vertex(pos=(2,4))
    g.add_vertex(pos=(2,5))
    
    g.add_vertex(pos=(3,1),etat='src')
    g.add_vertex(pos=(3,2))
    g.add_vertex(pos=(3,3))
    g.add_vertex(pos=(3,4))
    g.add_vertex(pos=(3,5))
    
    g.add_vertex(pos=(4,1))
    g.add_vertex(pos=(4,2))
    g.add_vertex(pos=(4,3))
    g.add_vertex(pos=(4,4))
    g.add_vertex(pos=(4,5),etat='dest')
    
    g.add_edge('11', [('12',7),('22',11)])  
    g.add_edge('12', [('13',7),('22',7)]) 
    g.add_edge('13', [('14',7),('23',7)]) 
    g.add_edge('14', [('15',7),('24',7),('25',7)]) 
    g.add_edge('15', [('25',7)]) 
    g.add_edge('21', [('22',7),('32',7)]) 
    g.add_edge('22', [('32',7),('23',1)]) 
    g.add_edge('23', [('14',2),('24',0.5),('33',7)]) 
    g.add_edge('24', [('15',7),('25',7),('35',0.7),('34',7)]) 
    g.add_edge('25', [('35',7)]) 
    g.add_edge('31', [('22',0.001),('32',700),('42',2),('45',2)]) 
    g.add_edge('32', [('33',7),('43',7),('42',7)]) 
    g.add_edge('33', [('24',7),('34',7),('44',7),('43',7)]) 
    g.add_edge('34', [('25',7),('35',7),('45',7),('44',7)]) 
    g.add_edge('35', [('45',100)]) 
    g.add_edge('41', [('42',7)]) 
    g.add_edge('42', [('43',1)]) 
    g.add_edge('43', [('34',7),('44',0.001)]) 
    g.add_edge('44', [('45',0.3)]) 
    
    
    g.drawGraph()
    
    pop = Population(g, 200, True)
    
    print("Première génération : ")
    pop.displayPop()
    print("Chemin initiale : " + str(pop.getFittest()))
    
    ga = GA(g)
    
    for i in range(0, 100):
        pop = ga.evoluerPopulation(pop)
        print("G-"+str(i+1))
        pop.displayPop()
        
    print("Chemin finale : " + str(pop.getFittest().getCout()))
    
    meilleurChemin = pop.getFittest().removeNones()
    #if(meilleurChemin.hasValideConnections()) : 
    g.drawGraph(meilleurChemin.convert_to_tuples())

 
    
 