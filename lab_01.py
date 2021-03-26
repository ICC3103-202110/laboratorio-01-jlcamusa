# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:10:32 2021

@author: pepo
"""

import random as rnd
import numpy as np

def imprimir(x):
    
    for i in x:
        print(*i)

def selector(x):
    lista=[]
    
    fila=int(input('Seleccione una fila: '))-1
    
    while fila>len(x)-1:
        print ('Esa fila no existe')
        fila=int(input('Seleccione una fila: '))-1
    
    columna=int(input('Seleccione una columna: '))-1
    
    while columna>len(x[0])-1:
        print ('Esa columna no existe')
        columna=int(input('Seleccione una columna: '))-1
        
    if oculto[fila][columna]==' ':
        print ('esa ficha no existe')
        print()
        imprimir(oculto)
        return selector(x)
    
    lista.append(fila)
    lista.append(columna)
    
    
    return lista


def division(L):
    if len(L)<=20:
        L1=[]
        L=np.array_split(L,2 )
        
        for i in L:
            L1.append(list(i))
        
        return L1
    else:
        L1=[]
        L=np.array_split(L,len(L)/10 )
        
        for i in L:
            L1.append(list(i))

        return L1
        
def turno(x):
    
    if contador[0]!=0:
        print('Turno '+ x)
    
        A=selector(Tablero)
    
        oculto[A[0]][A[1]]=Tablero[A[0]][A[1]]
    
        imprimir(oculto)
    
        A2=selector(Tablero)
        
        while A==A2:
            print('ya escogiste esa ficha')
            A2=selector(Tablero)
    
        oculto[A2[0]][A2[1]]=Tablero[A2[0]][A2[1]]
    
        imprimir(oculto)
        
        if Tablero[A[0]][A[1]]==Tablero[A2[0]][A2[1]] and x=='p2':
        
            p2[0]+=1
            contador[0]-=1
            oculto[A[0]][A[1]]=' '
            oculto[A2[0]][A2[1]]=' '
            turno(x)
        
        if Tablero[A[0]][A[1]]==Tablero[A2[0]][A2[1]] and x=='p1':
        
            p1[0]+=1
            contador[0]-=1
            oculto[A[0]][A[1]]=' '
            oculto[A2[0]][A2[1]]=' '
            turno(x)
        
        else:
            oculto[A[0]][A[1]]='*'
            oculto[A2[0]][A2[1]]='*'
    

cartas=int(input('Cantidad de cartas: '))

p1=[0]
p2=[0]

L=list(range(1,cartas+1))
L=L*2
rnd.shuffle(L)

oculto=['*']*len(L)
oculto=division(oculto)

Tablero=L
Tablero=division(Tablero)

imprimir(oculto)

contador=[cartas]
    
while contador[0]!=0:
    
    turno('p1')
    
    if contador[0]!=0:
        turno('p2')
    
if p1[0]>p2[0]:
    print('Gana p1')
if p1[0]<p2[0]:
    print('Gana p2')
if p1[0]==p2[0]:
    print('Es un empate')
    
    