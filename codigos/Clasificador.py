import pandas as pd
import spacy
import numpy as np

def classifier(dataframe):
    for col in cols:
        sustantivos_count = []
        verbos_count = []
        adjetivos_count = []
        adverbios_count = []
        for row in dataframe[col]:
            print('row: ',row)
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
                print('Sustantivos: ',sustantivos_count)
                print('Verbos: ', verbos_count)
                print('Adjetivos: ', adjetivos_count)
                print('Adverbios: ', adverbios_count)
        df_sustantivos[col+'_cuenta_sustantivos'] = pd.Series(sustantivos_count)
        df_verbos[col+'_cuenta_verbos'] = pd.Series(verbos_count)
        df_adjetivos[col+'_cuenta_adjetivos'] = pd.Series(adjetivos_count)
        df_adverbios[col+'_cuenta_adverbios'] = pd.Series(adverbios_count)

if __name__ == "__main__":
    nlp = spacy.load("es_core_news_md")
    cols = [ #empieza prueba 1
        #'idPersona',
        #'sexo',
        'clean_por_que_pelota_que_canta', #ok
        'clean_explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos', #ok
        'clean_que_otra_cosa_podria_ser_una_pelota_de_pelos', #ok
        'clean_explica_tu_respuesta_en_la_frase_pelota_de_plata', #ok
        'clean_c1t', #ok
        'clean_c2t', #ok
        'clean_c3t', #ok
        'clean_c4t', #ok 
        'clean_c5t', #ok
        'clean_c6t', #ok
        'clean_que_significa_1', #ok
        'clean_por_que_crees_que_si_o_no_es_posible_1', #ok
        'clean_que_significa_2', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_2', #ok
        'clean_que_significa_3', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_3', #error #ok
        'clean_que_significa_4', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_4', #ok 
        'clean_que_significa_5', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_5', #ok
        'clean_que_significa_6', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_6', #ok
        'clean_que_significa_7', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_7', #ok
        'clean_que_significa_8', #ok
        'clean_por_que_crees_que_si_o_que_no_es_posible_8', #ok
        'clean_que_significa_9', 
        'clean_por_que_crees_que_si_o_que_no_es_posible_9'
    ]
    df_sustantivos = pd.DataFrame()
    df_verbos = pd.DataFrame()
    df_adjetivos = pd.DataFrame()
    df_adverbios = pd.DataFrame()

    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/palabras_corregidas_primaria.csv'
    df = pd.read_csv(ruta_origen, encoding='latin1') #documento con muestras, modificar valor del argumento encoding por si arroja error al inicio
    classifier(df)
    df_sustantivos['suma_total_sustantivos'] = df_sustantivos.apply(np.sum, axis=1)
    df_verbos['suma_total_verbos'] = df_verbos.apply(np.sum, axis=1)
    df_adjetivos['suma_total_adjetivos'] = df_adjetivos.apply(np.sum, axis=1)
    df_adverbios['suma_total_adverbios'] = df_adverbios.apply(np.sum, axis=1)

    df_sustantivos.to_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/wilcox_test/Clasificación/Primaria/General/sustantivos_general_primaria.csv')
    df_verbos.to_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/wilcox_test/Clasificación/Primaria/General/verbos_general_primaria.csv')
    df_adjetivos.to_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/wilcox_test/Clasificación/Primaria/General/adjetivos_general_primaria.csv')
    df_adverbios.to_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/wilcox_test/Clasificación/Primaria/General/adverbios_general_primaria.csv')

