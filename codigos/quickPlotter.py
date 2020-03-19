import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint

import spacy
# from spacy import displacy


# Load Spanish tokenizer, tagger, parser, NER and word vectors
spa_lex = spacy.load('es_core_news_sm')


# imprime el nombre de las columnas
def colnames(df):
    for col in df.columns:
        columns = []  
        columns.append(str(col))
    print(columns)

# retorna solo los elementos unicos de un arreglo
def unique(array):
    unique_list = []
    for x in array:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# retorna solo los tokens limpios (quita espacios a la izquierda o derecha) de una columna
def colvals(df, colname):
    clean_collist = []
    collist = df[colname].tolist()
    for token in collist:
        token = token.strip()
        clean_collist.append(token)
    return clean_collist

# retorna un diccionario con los elementos de una arreglo y el conteo de apariciones de los mismos 
def countInstances(array):
    results = {}
    unique_elems = unique(array)
    instances = []
    counter = 0
    for unique_elem in unique_elems: # recorre el arreglo de unicos
        for instance_of_elem in array: # contador de instancias elementos unicos
            if str(unique_elem) == str(instance_of_elem):
                counter += 1
        instances.append(counter)
        counter = 0
    results['elements'] = unique_elems
    results['instances'] = instances
    return results

# Plotea 2 columnas, una de tokens y otra de valores o instancias, se evalua con <= threshold
# PARAMS
# xcol      - list
# colname   - str nombre del dato procesado ej. palabras, verbos, etc
# ycol      - list
# threshold - valor que evaluara el numero minimo de instancias
def quickPlot(coltitle, xcol, xcolname, ycol, threshold):
    if threshold != None:
        # construir un diccionario con las dos columnas (tokens e instancias). ej:
        # arr = { 'token':instancias,
        #     'token1':1,
        #     'token2':8 }
        arr_assoc = {}
        ignored_arr_assoc = {}
        pointer = 0

        # union paralela de dos arreglos ej [1,2,3] + [4,5,6] = [ [1,4],[2,5],[3,6] ]
        for token in xcol:
            arr_assoc[token] = ycol[pointer]
            pointer += 1

        # filtrado de values con el threshold
        for key, value in list(arr_assoc.items()):
            # condicion de evaluacion de los valores de la columna
            if value <= threshold:
                ignored_arr_assoc[key] = value
                del arr_assoc[key]

        # impresion de los elementos ignorados por el anterior filtro
        pprint(ignored_arr_assoc)

        # generacion de la grafica
        sorted_arr_assoc = {key: value for key, value in sorted(arr_assoc.items(), key=lambda item: item[1])}
        plt.bar(sorted_arr_assoc.keys(), sorted_arr_assoc.values())
        plt.xlabel(xcolname)
        plt.ylabel('Instancias')
        plt.title(coltitle + " | " + xcolname)
        plt.show()
    else:
        plt.bar(xcol, ycol)
        plt.title(coltitle + " | " + xcolname)
        plt.ylabel('Instancias')
        plt.title(coltitle)
        plt.show()

# funcion que procesa palabras
def processWords(df, colName):
    results = {}
    column = colvals(df, colName)

    # arreglos vacios donde se almacenan: la respuesta sin las stopwords, todos los verbos y todos los sustantivos
    clean_row = []
    
    sustantivos_total = []
    verbos_total      = []
    adjetivos_total   = []
    adverbios_total   = []
    clean_ans         = []

    tokens_per_row = []
    total_tokens = 0
    total_tokens_per_row = 0

    # for row in range(9,10):
    for row in range(len(column)): # iterar por cada row de la col
        doc = spa_lex(column[row])

        # sustantivos = [chunk.text for chunk in doc.noun_chunks] # para evaluar sustantivos con su determinante ej: el tomate
        sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
        verbos =      [token.lemma_ for token in doc if token.pos_ == "VERB"]
        adjetivos =   [token.lemma_ for token in doc if token.pos_ == "ADJ"]
        adverbios =   [token.lemma_ for token in doc if token.pos_ == "ADV"]

        sustantivos_total.extend(sustantivos)
        verbos_total.extend(verbos)
        adjetivos_total.extend(adjetivos)
        adverbios_total.extend(adverbios)

        for token in doc:
            total_tokens += 1
            total_tokens_per_row += 1
            if token.is_stop or token.is_punct or token.is_quote or len(token) == 1:
                pass # stopword
            # elif not token.is_stop and not token.is_punct and not token.is_quote and len(token) > 1 and (token.text in sustantivos or token.text in verbos):
            #     # si token no es stop, no es punt, no es comilla, mide mas de 1 y token es sustantivo o token es verbo
            #     # print(token)
            #     pass # palabra con falta de ortografia
            else:
                clean_row.append(token)
        
        tokens_per_row.append(total_tokens_per_row)
        clean_ans.append(clean_row)
        # print("---> Respuesta limpia: "+str(clean_row))
        # displacy.serve(doc, style="dep")
        total_tokens_per_row = 0
        clean_row = []
    results['nouns'] = sustantivos_total
    results['verbs'] = verbos_total
    results['adjts'] = adjetivos_total
    results['advbs'] = adverbios_total
    results['count'] = total_tokens
    results['tokens_row'] = tokens_per_row
    results['clean_ans'] = clean_ans
    return results

# Crea un df de Pandas a partir del conteo de instancias de nouns, verbs, adjts y advbs
def createDataframe(dataframe,column):
    result = processWords(dataframe, column)

    # Funciones para graficacion de instancias
    nouns = countInstances(result['nouns'])
    verbs = countInstances(result['verbs'])
    adjts = countInstances(result['adjts'])
    advbs = countInstances(result['advbs'])
    
    # Creacion de DataFrame, tienen que ser de tipo pd.Series para que no haya error si los arreglos son de diferente longitud
    result_df_dict = {
        column+"_clean_ans":   pd.Series(result['clean_ans'],name=column+"_clean_ans"),
        column+"_nouns":       pd.Series(nouns['elements'],  name=column+"_nouns"),
        column+"_nouns_count": pd.Series(nouns['instances'], name=column+"_nouns_count"),
        column+"_verbs":       pd.Series(verbs['elements'],  name=column+"_verbs"),
        column+"_verbs_count": pd.Series(verbs['instances'], name=column+"_verbs_count"),
        column+"_adjts":       pd.Series(adjts['elements'],  name=column+"_adjts"),
        column+"_adjts_count": pd.Series(adjts['instances'], name=column+"_adjts_count"),
        column+"_advbs":       pd.Series(advbs['elements'],  name=column+"_advbs"),
        column+"_advbs_count": pd.Series(advbs['instances'], name=column+"_advbs_count"),
        column+"_tokens":      pd.Series(result['count'],    name=column+"_tokens"),
        column+"_mean_tokens": pd.Series(np.mean(result['tokens_row']), name=column+"_mean_tokens")
    }

    result_df = pd.concat([
        result_df_dict[column+'_clean_ans'],
        result_df_dict[column+'_nouns'],
        result_df_dict[column+'_nouns_count'],
        result_df_dict[column+'_verbs'],
        result_df_dict[column+'_verbs_count'],
        result_df_dict[column+'_adjts'],
        result_df_dict[column+'_adjts_count'],
        result_df_dict[column+'_advbs'],
        result_df_dict[column+'_advbs_count'],
        result_df_dict[column+'_tokens'],
        result_df_dict[column+'_mean_tokens']
    ], axis=1)

    result_df = pd.DataFrame (result_df_dict, columns = [
        column+"_clean_ans",
        column+"_nouns",
        column+"_nouns_count",
        column+"_verbs",
        column+"_verbs_count",
        column+"_adjts",
        column+"_adjts_count",
        column+"_advbs",
        column+"_advbs_count",
        column+"_tokens",
        column+"_mean_tokens"
    ])

    return result_df


if __name__ == "__main__": # if que impide la ejecucion de este script si lo importamos como modulo
    # Reemplazar la ruta de abajo para obtener el CSV
    df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/SECUNDARIA_TODO.csv")
    col = "por_que_pelota_que_canta"

    # todas las columnas con texto a procesar
    all_cols = ['por_que_pelota_que_canta', 'explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos', 'por_que_pelota_de_pelos']
    
    # se crea el df, es necesario para poder hacer APPEND a el
    final_df = createDataframe(df, all_cols[0])

    # recorrer todas las columnas excepto la primera, pues ya se proceso y hacer APPEND al df original
    for col in range(1, len(all_cols)):
        temporal_df = createDataframe(df, all_cols[col])
        # temporal_df.to_csv("C:/Users/Drablaguna/Desktop/COUNT_"+str(col)+".csv", index=False)
        print(temporal_df)
        # final_df.append(temporal_df, ignore_index=True)
    
    # print(final_df)
    # final_df.to_csv("C:/Users/Drablaguna/Desktop/COUNT.csv", index=False)

    # print("\n======================= SUSTANTIVOS =======================")
    # quickPlot(col, nouns['elements'], 'Sustantivos', nouns['instances'], 5)
    # print("\n======================= VERBOS =======================")
    # quickPlot(col, verbs['elements'], 'Verbos', verbs['instances'], 5)
    # print("\n======================= ADJETIVOS =======================")
    # quickPlot(col, adjts['elements'], 'Adjetivos', adjts['instances'], 5)
    # print("\n======================= ADVERBIOS =======================")
    # quickPlot(col, advbs['elements'], 'Adverbios', advbs['instances'], 5)

    # print("\n---> Total tokens: " + str(result['count']))
    # print("---> Promedio de tokens por fila: " + str(np.mean(result['tokens_row'])))

    """
    # Reemplazar el nombre de la columna que se quiere evaluar
    a1 = colvals(df, 'el_es_una_pelota_de_fuego')
    res = countInstances(a1)
    # Generacion de la grafica, el ultimo numero indica el valor que se evaluara para determinar los elementos que se graficaran
    # ej. Si es 3, todos los elementos cuyas instancias sean de 3 o menos no se graficaran pero se imprimiran en consola
    quickPlot(res['elements'],res['instances'], 3, True)
    # quickPlot(res['elements'],res['instances'], None)
    """
    