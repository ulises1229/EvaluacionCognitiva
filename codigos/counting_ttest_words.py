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
            print("Oración: ",x)
            res = sum([i.strip(string.punctuation).isalpha() for i in x.split()]) #res es el conteo limpio de los datos, sin contar los espacios ni las signos
            print ("Numero de palabras: " +  str(res)) 
            total_palabras_col += res
    #print("total de palabras hasta ahora: ", total_palabras_col)
    total_col = pd.Series(total_palabras_col)
    new_df[col+'_count_total'] = total_col
    return total_palabras_col

def main():
    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/SECUNDARIA_MUJERES.csv'
    df = pd.read_csv(ruta_origen, encoding='latin1') #documento con muestras, modificar valor del argumento encoding por si arroja error al inicio
    cols = [ #empieza prueba 1
        'idPersona',
        'sexo',
        'por_que_pelota_que_canta', #ok
        'explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos', #ok
        'que_otra_cosa_podria_ser_una_pelota_de_pelos', #ok
        'explica_tu_respuesta_en_la_frase_pelota_de_plata', #ok
        'c1t', #ok
        'c2t', #ok
        'c3t', #ok
        'c4t', #ok 
        'c5t', #ok
        'c6t', #ok
        'que_significa_1', #ok
        'por_que_crees_que_si_o_no_es_posible_1', #ok
        'que_significa_2', #ok
        'por_que_crees_que_si_o_que_no_es_posible_2', #ok
        'que_significa_3', #ok
        'por_que_crees_que_si_o_que_no_es_posible_3', #error #ok
        'que_significa_4', #ok
        'por_que_crees_que_si_o_que_no_es_posible_4', #ok 
        'que_significa_5', #ok
        'por_que_crees_que_si_o_que_no_es_posible_5', #ok
        'que_significa_6', #ok
        'por_que_crees_que_si_o_que_no_es_posible_6', #ok
        'que_significa_7', #ok
        'por_que_crees_que_si_o_que_no_es_posible_7', #ok
        'que_significa_8', #ok
        'por_que_crees_que_si_o_que_no_es_posible_8', #ok
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
    ruta_destino = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/counteo_secundaria_mujeres.csv' #cambiar ruta destino al gusto
    array_numpy = np.array(tot_values_list)
    mean = pd.Series(np.mean(array_numpy))
    values = pd.Series(tot_values_list)
    new_df['lista_de_valores'] = values
    new_df['promedio_total'] = mean
    print('CSV obtenido de: ', ruta_origen)
    print('Generando csv en: ',ruta_destino)
    new_df.to_csv(ruta_destino)



if __name__ == "__main__":
    main()
    




