#Aplicación para conteo de palabras por alumno y realizar prueba T de las medias
#1.- Leer fila perteneciente a cada alumno
#2.- Contar las palabras que se encuentren ahí 
#3.- Sumar cada cifra resultante de cada fila de datos de los alumnos
#4.- Crear tres data frames, uno con hombres, otro con mujeres, y otro con hombres y mujeres
#5.- Sacar media de hombres y de mujeres de cifras de palabras
#6.- Realizar prueba T de estos

#import spacy as sp
import numpy as np
import pandas as pd
import string

#¿cuantos dataframes serían en total?: uno para los hombres de primaria, otro para las mujeres de primaria, y un último de los 2
#ahora bien, que hay en común entre ellos? 
#suma total por niño
#suma total por columna
#primero hacer cuentas y guardarlas, ¿como? listas? cómo quedaría output esperado?

def count_words(data, col, new_df):
    total_palabras_col = 0
    for x in data:
        if x == 'NS' or x == '0' or x == 'NN' or x == 'WW' or x == '-':
            pass
        else:
            #print("Oración: ",x)
            res = sum([i.strip(string.punctuation).isalpha() for i in x.split()]) #res es el conteo limpio de los datos, sin contar los espacios ni las signos
           # print ("Numero de palabras: " +  str(res)) 
            total_palabras_col += res
    #print("total de palabras hasta ahora: ", total_palabras_col)
    total_col = pd.Series(total_palabras_col)
    new_df[col+'_count_total'] = total_col
    return total_palabras_col

def main():
    df = pd.read_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/SECU_TODO_CLEAN.csv', encoding='latin1') #documento con muestras, modificar valor del argumento encoding por si arroja error al inicio
    cols = [ #empieza prueba 1
        'idPersona',
        'sexo',
        'por_que_pelota_que_canta',
        'explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos',
        'que_otra_cosa_podria_ser_una_pelota_de_pelos',
        'explica_tu_respuesta_en_la_frase_pelota_de_plata',
        'c1t',
        'c2t',
        'c3t',
        'c4t',
        'c5t',
        'c6t',
        'que_significa_1',
        'por_que_crees_que_si_o_no_es_posible_1',
        'que_significa_2',
        'por_que_crees_que_si_o_que_no_es_posible_2',
        'que_significa_3',
        'por_que_crees_que_si_o_que_no_es_posible_3', #error
        'que_significa_4',
        'por_que_crees_que_si_o_que_no_es_posible_4',
        'que_significa_5',
        'por_que_crees_que_si_o_que_no_es_posible_5',
        'que_significa_6',
        'por_que_crees_que_si_o_que_no_es_posible_6',
        'que_significa_7',
        'por_que_crees_que_si_o_que_no_es_posible_7',
        'que_significa_8',
        'por_que_crees_que_si_o_que_no_es_posible_8',
        'que_significa_9',
        'por_que_crees_que_si_o_que_no_es_posible_9'
    ]
    tot_values_list = []
    new_df = pd.DataFrame()
    for sent in cols:
        new_col = pd.Series(df[sent])
        new_df[sent] = new_col
       #print(new_df)
        if sent != 'idPersona' and sent != 'sexo':
            tot = count_words(df[sent], sent, new_df)
            tot_values_list.append(tot)
            #print('lista de palabras: ',tot_values_list)
        else:
            pass
    
    array_numpy = np.array(tot_values_list)
    mean = pd.Series(np.mean(array_numpy))
    values = pd.Series(tot_values_list)
    new_df['lista_de_valores'] = values
    new_df['promedio_total'] = mean
    new_df.to_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/codigos/counting_secundaria.csv')



if __name__ == "__main__":
    main()
    




