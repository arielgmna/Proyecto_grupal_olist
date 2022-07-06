import pandas as pd
import numpy as np
def analizador(nombre):
    direccion='e-comerce_Olist_dataset/'+nombre+'.csv'
    csv=pd.read_csv(direccion)
    print('Dimensiones:', csv.shape)
    print('Número de elemntos:', csv.size) 
    print('Nombres de columnas:', csv.columns) 
    print('Nombres de filas:', csv.index) 
    print('Tipos de datos:\n', csv.dtypes) 
    print('Primeras 10 filas:\n', csv.head(10)) 
    print('Últimas 10 filas:\n', csv.tail(10))
    print('info general del dataset:\n', csv.info())
    
def main():
    csv= input('nombrar el dataset: ')
    info=analizador(csv)

main()