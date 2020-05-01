import numpy as np
import pandas as pd
import string

def count_words(vec, col, dataframe):
    list_of_count = []
    for x in vec:
        if x == 'NS' or x == '0' or x == 'NN' or x == 'WW' or x == '-':
            res = 0
            list_of_count.append(res)
        else:
            res = sum([i.strip(string.punctuation).isalpha() for i in x.split()]) #res es el conteo limpio de los datos, sin contar los espacios ni las signos
            list_of_count.append(res)
    return list_of_count

def main():
    ruta_origen = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/SECUNDARIA_MUJERES.csv'
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
    ruta_destino = 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Secundaria/conteo_secundaria_mujeres.csv'
    new_df = pd.DataFrame()
    for sent in cols:
        if sent != 'idPersona' and sent != 'sexo':
            list_values = count_words(df[sent], sent, new_df)
            new_df[sent+'_count'] = pd.Series(list_values)
    new_df['suma_total'] = new_df.apply(np.sum, axis=1)
    print('Generando csv en: ', ruta_destino)
    new_df.to_csv(ruta_destino)
if __name__ == "__main__":
    main()
    




