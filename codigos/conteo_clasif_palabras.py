import numpy as np
import pandas as pd
import string
from hunspell import Hunspell
import sys
#import spacy

def row_x_row(vec):
    for row in vec:
        cleaned_row = clean_row(row)
        return cleaned_row

def classifier(word):
    list_of_adv = []
    list_of_verb = []
    list_of_adj = []
    list_of_sust = []
    pass

def analyzer(strings_list):
    new_sentence = " "
    sentence = ''.join(strings_list)
    for string in strings_list:
        print("analizando oración: {}".format(sentence))
        if h.spell(string) == True:
            print("palabra: {}, es correcta.".format(string))
            pass
        elif h.spell(string) == False:
            print("palabra: {}, es incorrecta. Es necesario cambiarla".format(string))
            list_suggests = list(h.suggest(string))
            for i, value in enumerate(list_suggests, 0):
                print("{} ->{}".format(i, value))
            value = input("Elige la palabra que mejor se adapta o reescribe la oración:")
            try:
                val = int(value)
                print("Has elegido la opción: {} ó -> {}".format(val, list_suggests[val]))
                index = strings_list.index(string)
                strings_list[index] = list_suggests[val]
                print("index: {}".format(index))
            except ValueError:
                print("No has elegido nada")
    return new_sentence.join(strings_list)
                
            

def clean_row(row):
    print("Antes de limpieza: {}".format(row))
    cleaner = str.maketrans('', '', string.punctuation)
    clean_row = row.translate(cleaner).split()
    print("Después de la limpieza, en lista: {}".format(clean_row))
    analisis = analyzer(clean_row)
    return analisis


def main():
    list_of_rows = []
    clean_dataframe = pd.DataFrame()
    for col in cols:
        if col != "idPersona" and col != "sexo":
            row =  row_x_row(df[col])
            list_of_rows.append(row)
            print("row nuevo: ",list_of_rows)
    #classifier()
            

if __name__ == "__main__":
    h = Hunspell('es_MX',hunspell_data_dir='C:/Users/Alex Isasi/AppData/Local/Programs/Python/Python37/Lib/site-packages/dictionaries')
    #nlp = spacy.load("es_core_news_md")
    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/PRIMARIA_TODO.csv'
    ruta_destino = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/conteo_clasificatorio_general.csv'
    print('Recopilando datos de: ',ruta_origen)
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
    main()
