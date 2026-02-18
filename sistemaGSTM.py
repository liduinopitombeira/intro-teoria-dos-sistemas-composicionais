# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:25:37 2023

@author: GESC
"""


from random import *
from copy import *
from music21 import *



#GERAÇÃO


def GER(quantidade):

    classes_de_notas = list(range(12))
    
    return [sample(classes_de_notas,3) for x in range(quantidade)]


# Função auxiliar para a geração do ritmo harmônico
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p
            

def chord_dur(n):
    
    dur_total = sum(n)
    
    partition = list(partitions(dur_total)) 
    partition_ = choice(partition)
    
    return partition_
    
       


#TRANSFORMAÇÃO

# Transpõe o conjunto por um fator k
def T(cn,k):
    
    return (cn + k)%12
    
# Inverte em torno de 0 e transpõe por um fator k
def I(cn,k):
    
    return (12- cn + k)%12



#SELEÇÃO


#Seleciona o caminho transformacional que terão os dados de entrada
def SEL(E,k):

    chaves = [0,1]
    S = []
    
    for x in E:
        seletor = choice(chaves)
        # print(seletor)
        if seletor==0: 
            valor = T(x,k)
            S.append(valor)
            # print(valor)
        if seletor==1: 
            valor = I(x,k)
            S.append(valor)
            # print(valor)
        
    return S

#MAPEAMENTO

#Define as durações (iniciando em 1)
def MAP(E):

    R = deepcopy(E)
    return [(x+1) for x in R]




#ENTRADA

E = input('Entre com uma lista de classes de alturas separadas por espaço: ').split()
E = [int(x) for x in E]

S = SEL(E,2)
durations = MAP(E)
ritmo_harmonico = chord_dur(durations)
acordes = GER(len(ritmo_harmonico))

# Criar um objeto Score que conterá as partes
score = stream.Score()

# Crie uma Stream para a linha melódica
melody_stream = stream.Part()

# Crie objetos Note para a linha melódica e defina suas durações
for i, note_class in enumerate(S):
    
    nota = note.Note(note_class)
    nota.quarterLength = durations[i]/2
    melody_stream.append(nota)

# Crie uma Stream para os acordes
chord_stream = stream.Part()

# Associe cada acorde a uma duração correspondente no ritmo harmônico
for i, chord_classes in enumerate(acordes):
    
    acorde = chord.Chord(chord_classes)
    acorde.quarterLength = ritmo_harmonico[i]/2
    chord_stream.append(acorde)


# Adicionar as partes ao score
score.insert(0, melody_stream)
score.insert(0, chord_stream)

#Visualizar o score
# score.show()

partitura = score.write('musicxml', fp='gstm_2.mxl')










