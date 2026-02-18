# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:07:10 2023

@author: GESC
"""

from music21 import *
from random import *

def pitch_space_to_midi(note):
    
        
    reference_midi = 60  # MIDI note number for middle C
    reference_pitch = 0  # Corresponding pitch space value

    # Calculate the pitch space value based on the reference
    midi_value = note + reference_midi
    
    if midi_value>=91: midi_value= midi_value -12

    return midi_value

def midi_to_pitch_space(midi_note):
    reference_midi = 60  # MIDI note number for middle C
    reference_pitch = 0  # Corresponding pitch space value

    # Calculate the pitch space value based on the reference
    pitch_space_value = midi_note - reference_midi

    return pitch_space_value

def SOMA (x,k):
    return x+k

def SUB (x,k):
    return x-k

def MULT (x,k):
    return x*k


#Lê um arquivo MIDI


#Extract the pitch parameter from a MIDI file
entrada = converter.parse('Promenademelodia.mxl').flat.getElementsByClass('Note')


alturas = [x.pitch.midi for x in entrada]
ritmo = [x.quarterLength for x in entrada]


E = [midi_to_pitch_space(x) for x in alturas]


k = int(input('Entre com o valor de k: '))


#Seletor

chaves = [0,1,2]
S = []

for x in range(len(E)):
    seletor = choice(chaves)
    # print(seletor)
    if seletor==0: 
        valor = SOMA(E[x],k)
        S.append(valor)
        # print(valor)
    if seletor==1: 
        valor = SUB(E[x],k)
        S.append(valor)
        # print(valor)
    if seletor==2:
        valor = MULT(E[x],k)
        S.append(valor)
        # print(valor)


S = [pitch_space_to_midi(x) for x in S]  

melodic_line = stream.Stream()

for i in range(len(S)):
    nota = note.Note(S[i])
    nota.quarterLength = ritmo[i]
    melodic_line.append(nota)
    
melodic_line.write('musicxml', 'Promenadealterado.musicxml')

melodic_line.show('musicxml')




