import matplotlib.pyplot as plt
import pandas as pd
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
    collist = []
    clean_collist = []
    collist = df[colname].tolist()
    for token in collist:
        token = token.strip()
        clean_collist.append(token)
    return clean_collist

# retorna un diccionario con los elementos de una columna y el conteo de apariciones de los mismos 
def countInstances(colvals):
    results = {}
    unique_elems = unique(colvals)
    instances = []
    counter = 0
    for unique_elem in unique_elems: # recorre el arreglo de unicos
        for instance_of_elem in colvals: # contador de instancias elementos unicos
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


# funcion que clasifica palabras
def classifyWords(df, colName):
    column = colvals(df, colName)
    # un arreglo vacio donde se almacenara la respuesta sin las stopwords
    clean_row = []
    # iterar por cada row de la col
    for row in range(1,2):
        doc = spa_lex(column[row])
        print("Respuesta: "+str(doc))
        print("Sustantivos:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbos:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        for token in doc:
            # quitar stopwords
            if token.is_stop or token.is_punct or token.is_quote or len(token) == 1:
                print(token)
            else:
                clean_row.append(token)

        print("Respuesta limpia: "+str(clean_row))
        displacy.serve(doc, style="dep")
        # se reinicia el arreglo de tokens
        clean_row = []
        print("\n")

# if que impide la ejecucion de este script si lo importamos como modulo
if __name__ == "__main__":    
    # Reemplazar la ruta de abajo para obtener el CSV
    df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/SECUNDARIA_TODO.csv")
    classifyWords(df, "por_que_pelota_que_canta")
    """
    # Reemplazar el nombre de la columna que se quiere evaluar
    a1 = colvals(df, 'el_es_una_pelota_de_fuego')
    res = countInstances(a1)
    # Generacion de la grafica, el ultimo numero indica el valor que se evaluara para determinar los elementos que se graficaran
    # ej. Si es 3, todos los elementos cuyas instancias sean de 3 o menos no se graficaran pero se imprimiran en consola
    quickPlot(res['elements'],res['instances'], 3, True)
    # quickPlot(res['elements'],res['instances'], None)
    """