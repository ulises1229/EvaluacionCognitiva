import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint

import spacy
from spacy import displacy


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

# genera un CSV con la lista pasada como param y lo guarda en el directorio raiz, NO lo retorna
# la lista como param tendra el nombre de las columnas
def generateCSV(colnames_list, base_dict, filename):
    pass

# plotea 2 columnas, una de tokens y otra de valores o instancias, se evalua con <= threshold
# PARAMS
# xcol - list
# ycol - list
# threshold - valor que evaluara el numero minimo de instancias
# genCSV - True o False, permite la generacion o no de un CSV de los elementos ignorados por el threshold
def quickPlot(xcol, ycol, threshold, genCSV):
    if threshold != None:
        # construir un diccionario con las dos columnas (tokens e instancias). ej:
        # arr = { 'token':instancias,
        #     'token1':1,
        #     'token2':8 }
        arr_assoc = {}
        ignored_arr_assoc = {}
        pointer = 0
        for token in xcol:
            arr_assoc[token] = ycol[pointer]
            pointer += 1
        pointer = 0

        # filtrado de values con el threshold
        for key, value in list(arr_assoc.items()):
            # condicion de evaluacion de los valores de la columna
            if value <= threshold:
                ignored_arr_assoc[key] = value
                del arr_assoc[key]

        # impresion de los elementos ignorados por el anterior filtro
        print(ignored_arr_assoc)
        # impresion de los elementos ignorados por el anterior filtro
        # if genCSV == True:
        #     generateCSV(['Palabra','Instancias'],ignored_arr_assoc,'El _ es una pelota de fuego')

        # generacion de la grafica
        sorted_arr_assoc = {key: value for key, value in sorted(arr_assoc.items(), key=lambda item: item[1])}
        plt.bar(sorted_arr_assoc.keys(), sorted_arr_assoc.values())
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')
        plt.show()
    else:
        plt.bar(xcol, ycol)
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')
        plt.show()


# funcion que procesa palabras
def processWords(df, colName):
    results = {}
    column = colvals(df, colName)
    # arreglos vacios donde se almacenan: la respuesta sin las stopwords, todos los verbos y todos los sustantivos
    clean_row = []
    sustantivos_total = []
    verbos_total = []
    tokens_per_row = []
    total_tokens = 0
    total_tokens_per_row = 0
    # iterar por cada row de la col
    for row in range(len(column)):
    # for row in range(1,10):
        doc = spa_lex(column[row])
        # print("---> Respuesta: "+str(doc))
        # sustantivos = [chunk.text for chunk in doc.noun_chunks] # para evaluar sustantivos con su determinante ej: el tomate
        sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
        verbos = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        # print("---> Sustantivos: ", sustantivos)
        # print("---> Verbos: ", verbos)
        sustantivos_total.extend(sustantivos)
        verbos_total.extend(verbos)

        for token in doc:
            total_tokens += 1
            total_tokens_per_row += 1
            if token.is_stop or token.is_punct or token.is_quote or len(token) == 1:
                pass # stopword
            elif not token.is_stop and not token.is_punct and not token.is_quote and len(token) > 1 and (token.text in sustantivos or token.text in verbos):
                # si token no es stop, no es punt, no es comilla, mide mas de 1 y token es sustantivo o token es verbo
                # print(token)
                pass # palabra con falta de ortografia
            else:
                clean_row.append(token)
        
        tokens_per_row.append(total_tokens_per_row)
        total_tokens_per_row = 0
        # print("---> Respuesta limpia: "+str(clean_row))
        # displacy.serve(doc, style="dep")
        clean_row = []
    results['nouns'] = sustantivos_total
    results['verbs'] = verbos_total
    results['count'] = total_tokens
    results['tokens_row'] = tokens_per_row
    return results

# if que impide la ejecucion de este script si lo importamos como modulo
if __name__ == "__main__":
    # Reemplazar la ruta de abajo para obtener el CSV
    df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/SECUNDARIA_TODO.csv")
    result = processWords(df, "por_que_pelota_que_canta")
    # print(result)
    print("---> Total tokens: " + str(result['count']))
    print("---> Promedio de tokens por fila: " + str(np.mean(result['tokens_row'])))
    nouns = countInstances(result['nouns'])
    verbs = countInstances(result['verbs'])
    # quickPlot(nouns['elements'],nouns['instances'], 5, True)
    # quickPlot(verbs['elements'],verbs['instances'], 5, True)
    """
    # Reemplazar el nombre de la columna que se quiere evaluar
    a1 = colvals(df, 'el_es_una_pelota_de_fuego')
    res = countInstances(a1)
    # Generacion de la grafica, el ultimo numero indica el valor que se evaluara para determinar los elementos que se graficaran
    # ej. Si es 3, todos los elementos cuyas instancias sean de 3 o menos no se graficaran pero se imprimiran en consola
    quickPlot(res['elements'],res['instances'], 3, True)
    # quickPlot(res['elements'],res['instances'], None)
    """