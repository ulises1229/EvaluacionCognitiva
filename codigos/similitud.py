import pandas as pd
import spacy
from quickPlotter import colnames, unique, colvals, countInstances

"""
Hace una evaluacion simple de similitud entre todas las columnas con respuestas evaluadas con menos de 3 con
respuestas evaluadas con 3, el metodo es el siguiente:

frase 1: la mujer corre
frase 2: el hombre salta

El algoritmo de similitud compara cada token con cada token y retorna una evaluacion numerica entre 0 y 1 basada
en el diccionario de vectores que importamos:

la    -> el     -> 0.9
la    -> hombre -> 0.3
la    -> salta  -> 0.1

mujer -> el     -> 0.5
mujer -> hombre -> 0.7
mujer -> salta  -> 0.1

corre -> el     -> 0.1
corre -> hombre -> 0.2
corre -> salta  -> 0.6

Y para encontrar la similitud entre oraciones se calcula un promedio de estas comparaciones:

0.9 + 0.3 + 0.1 + 0.5 + 0.7 + 0.1 + 0.1 + 0.2 + 0.6 / 9 = 0.38

"""

spa_lex = spacy.load('es_core_news_md') # inicializamos el diccionario mediano, hay que descargarlo del sitio web de spacy

df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/SECU_TODO_CLEAN.csv") # reemplazar ruta para otro CSV


def evalChar(x): # usada en cleanString, contiene todos los caracteres especiales a eliminar de un string
    if x in [",",".",":",";","`","'",'"',"(",")","-","_","~","/","?","¿","="]:
        x = ""
    return x

def cleanString(x): # funcion que limpia string de caracteres especiales especificados en evalChar
    s = map(evalChar, x)
    s = "".join(list(s))
    return s

def analize(base, comparer):
    """Proceso completo de analisis"""
    for token_base in base:
        for token_toCompare in comparer:
            t1 = token_base.text
            t2 = token_toCompare.text
            simil = token_base.similarity(token_toCompare)
            results['token_base'].append(t1)
            results['token_toCompare'].append(t2)
            results['similarity'].append(simil)


# obtengo todos los valores de dos columnas
df_base = df[['explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos', 'a5']]

# todas las filas que sean evaluadas con todo menos 3
df1 = df_base.loc[df_base['a5'] < 3]
df1_list_clean = list(map(cleanString, df1['explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos']))

# todas las filas que sean evaluadas con 3
df2 = df_base.loc[df_base['a5'] == 3]
df2_list_clean = list(map(cleanString, df2['explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos']))

# variables globales
row_count = 1
# todos los resultados son arreglos que se pueden unir paralelamente
results = {
    'token_base': [],      # tokens originales
    'token_toCompare': [], # token con el que se comparo
    'similarity': [],      # valor de la similitud de ambos
    'total_sim_mean': 0    # promedio similitud por frase
}

# cada respuesta evaluada a 3
for master_row in df2_list_clean:
    master_row = spa_lex(master_row)
    print("---> Master_row " + str(row_count) + ": " + str(master_row))
    print("---> Results: ")
    print(results)
    # sera evaluada con todas las respuestas menores a 3
    for row in df1_list_clean:
        row = spa_lex(row)
        analize(master_row, row)
    row_count += 1

results['total_sim_mean'] = 0
print(results)