import numpy as np
import pandas as pd
import string
from hunspell import Hunspell
import sys
import spacy

def row_x_row(vector, column):
    list_of_values = []
    for row in vector:
        if row == 'NS' or row == '0' or row == 'NN' or row == 'WW' or row == '-':
            pass
        else:
            cleaned_row = clean_row(row)
            print("Oración limpia: ",cleaned_row)
            list_of_values.append(cleaned_row)
            #print('Valores hasta ahora: ',list_of_values)
    new_df['clean_'+column] = pd.Series(list_of_values)
    
def classifier(dataframe):
    for col in cols:
        sustantivos_count = []
        verbos_count = []
        adjetivos_count = []
        adverbios_count = []
        for row in dataframe[col]:
            if row == 'NS' or row == '0' or row == 'NN' or row == 'WW' or row == '-':
                sustantivos_count.append(0)
                verbos_count.append(0)
                adjetivos_count.append(0)
                adverbios_count.append(0)
            else:
                sustantivos = []
                verbos = []
                adjetivos = []
                adverbios = []
                doc = nlp(row)
                for word in doc:
                    if word.pos_ == "NOUN":
                        sustantivos.append(word.text)
                    elif word.pos_ == "VERB":
                        verbos.append(word.text)
                    elif word.pos_ == "ADJ":
                        adjetivos.append(word.text)
                    elif word.pos_ == "ADV":
                        adverbios.append(word.text)
                sustantivos_count.append(len(sustantivos))
                verbos_count.append(len(verbos))
                adjetivos_count.append(len(adjetivos))
                adverbios_count.append(len(adverbios))
            df_sustantivos[col+'_cuenta_sustantivos'] = pd.Series(sustantivos_count)
            df_verbos[col+'_cuenta_verbos'] = pd.Series(verbos_count)
            df_adjetivos[col+'_cuenta_adjetivos'] = pd.Series(adjetivos_count)
            df_adverbios[col+'_cuenta_adverbios'] = pd.Series(adverbios_count)

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
            value = input("Elige la palabra que mejor se adapta o escribe la palabra correcta:")
            try:
                val = int(value)
                print("Has elegido la opción: {} ó -> {}".format(val, list_suggests[val]))
                strings_list[index] = list_suggests[val]
                print("index: {}".format(index))
            except ValueError:
                strings_list[index] = value
    return " ".join(strings_list)
                
            

def clean_row(row):
    print("Antes de limpieza: {}".format(row))
    cleaner = str.maketrans('', '', string.punctuation)
    clean_row = row.translate(cleaner).split()
    print("Después de la limpieza, en lista: {}".format(clean_row))
    analisis = analyzer(clean_row)
    return analisis


def main():
    for col in cols:
        if col != "idPersona" and col != "sexo":
            row_x_row(df[col], col)  #esto regresará data frame con palabras analizadas y limpias
    new_df.to_csv(ruta_destino)
    print("Fin de limpieza, comienza clasificación.")
    classifier(new_df)
    df_sustantivos.to_csv('C:/Users/Alex Isasi/Desktop/HUNSPELL/pruebas/sustantivos.csv')
    df_verbos.to_csv('C:/Users/Alex Isasi/Desktop/HUNSPELL/pruebas/verbos.csv')
    df_adjetivos.to_csv('C:/Users/Alex Isasi/Desktop/HUNSPELL/pruebas/adjetivos.csv')
    df_adverbios.to_csv('C:/Users/Alex Isasi/Desktop/HUNSPELL/pruebas/adverbios.csv')

            

if __name__ == "__main__":
    h = Hunspell('es_MX',hunspell_data_dir='C:/Users/Alex Isasi/AppData/Local/Programs/Python/Python37/Lib/site-packages/dictionaries')
    nlp = spacy.load("es_core_news_md")
    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/PRIMARIA_TODO.csv'
    ruta_destino = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/palabras_limpias.csv'
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
    new_df = pd.DataFrame()
    df_sustantivos = pd.DataFrame()
    df_verbos = pd.DataFrame()
    df_adjetivos = pd.DataFrame()
    df_adverbios = pd.DataFrame()
    main()
