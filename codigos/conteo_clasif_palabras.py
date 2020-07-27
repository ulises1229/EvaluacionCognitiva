simport numpy as np
import pandas as pd
import string
from hunspell import Hunspell
import sys
#import spacy

class Dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):  #Agregará palabras no recnocidas por Hunspell al nuevo diccionario
        self[key] = value

    def check(self, key):    #Checará si la palabra escrita está en el diccionario
        if key in self:
            print('La palabra si está en el diccionario')
            return True
        else:
            print('La palabra no está en el diccionario')
            return False

    def values_returner(self, key):  #Regresará el valor de la llave buscada
        print('El valor devuelto de {} es: {}'.format(key, self[key]))
        return self[key]

def row_x_row(vector, column):
    list_of_values = []
    for row in vector:
        if row == 'NS' or row == '0' or row == 'NN' or row == 'WW' or row == '-':
            list_of_values.append('0')
        else:
            cleaned_row = clean_row(row)
            #print("Oración limpia: ",cleaned_row)
            list_of_values.append(cleaned_row)
            #print('Valores hasta ahora: ',list_of_values)
    new_df['clean_'+column] = pd.Series(list_of_values)

def analyzer(strings_list):
    sentence = ' '.join(strings_list)
    print("analizando oración: {}".format(sentence))
    for string in strings_list:
        if h.spell(string) == True:
            pass
        elif h.spell(string) == False:
            print("palabra: {}, es incorrecta. Es necesario cambiarla".format(string))
            list_suggests = list(h.suggest(string))
            for i, value in enumerate(list_suggests, 0):
                print("{} ->{}".format(i, value))
            index = strings_list.index(string)
            print('Diccionario hasta ahora: ',my_dict)
            if my_dict.check(strings_list[index]) == True:
                strings_list[index] = my_dict.values_returner(strings_list[index])
            else:
                value = input("Elige la palabra que mejor se adapta o escribe la palabra correcta:")
                try:
                    val = int(value)
                    #print("Has elegido la opción: {} ó -> {}".format(val, list_suggests[val]))
                    strings_list[index] = list_suggests[val]
                    my_dict.add(string, list_suggests[val])
                   # print("index: {}".format(index))
                
                except IndexError:
                    pass

                except ValueError:
                    strings_list[index] = value
                    decision = input("¿Agregar al diccionario? si/ cualquier tecla")
                    if decision == 'si':
                        my_dict.add(string, value)
                    else: 
                        pass
    return " ".join(strings_list)

def clean_row(row):
    #print("Antes de limpieza: {}".format(row))
    cleaner = str.maketrans('', '', string.punctuation)
    clean_row = row.translate(cleaner).split()
    #print("Después de la limpieza, en lista: {}".format(clean_row))
    analisis = analyzer(clean_row)
    return analisis


def main():
    for col in cols:
        if col != "idPersona" and col != "sexo":
            row_x_row(df[col], col)  #esto regresará data frame con palabras analizadas y limpias
    new_df.to_csv(ruta_destino)
    print("Fin de limpieza, comienza clasificación.")
            

if __name__ == "__main__":
    h = Hunspell('es_MX',hunspell_data_dir='C:/Users/Alex Isasi/AppData/Local/Programs/Python/Python37/Lib/site-packages/dictionaries')
    #nlp = spacy.load("es_core_news_md")
    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/SECU_TODO_CLEAN.csv'
    ruta_destino = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/palabras_limpias_faltante.csv'
    print('Recopilando datos de: ',ruta_origen)
    df = pd.read_csv(ruta_origen, encoding='latin1') #documento con muestras, modificar valor del argumento encoding por si arroja error al inicio
    cols = [
        'por_que_pelota_de_pelos'
        #empieza prueba 1
        #'idPersona',
        #'sexo',
        #'por_que_pelota_que_canta', #ok
        #'explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos', #ok
        #'que_otra_cosa_podria_ser_una_pelota_de_pelos', #ok
        #'explica_tu_respuesta_en_la_frase_pelota_de_plata', #ok
        #'c1t', #ok
        #'c2t', #ok
        #'c3t', #ok
       # 'c4t', #ok 
        #'c5t', #ok
        #'c6t', #ok
        #'que_significa_1', #ok
        #'por_que_crees_que_si_o_no_es_posible_1', #ok
        #'que_significa_2', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_2', #ok
        #'que_significa_3', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_3', #error #ok
        #'que_significa_4', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_4', #ok 
        #'que_significa_5', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_5', #ok
        #'que_significa_6', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_6', #ok
        #'que_significa_7', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_7', #ok
        #'que_significa_8', #ok
        #'por_que_crees_que_si_o_que_no_es_posible_8', #ok
       # 'que_significa_9', 
        #'por_que_crees_que_si_o_que_no_es_posible_9'
    ]
    my_dict = Dictionary()
    new_df = pd.DataFrame()
    main()