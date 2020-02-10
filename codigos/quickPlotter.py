import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getCSV(filePath):
    df = pd.read_csv(filePath)
    return df

def colnames(df):
    for col in df.columns:
        columns = []  
        columns.append(str(col))
    print(columns)

def unique(array):
    unique_list = []
    for x in array:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def colvals(df, colname):
    collist = []
    collist = df[colname].tolist()
    return collist

def count(colvals):
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

def quickPlot(xcol, ycol, color):
    if color == None:
        plt.bar(xcol, ycol) 
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')	
    else:
        plt.bar(xcol, ycol) 
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')	
    plt.show()


# ['np',
    #  'apellido paterno',
    #  'apellido materno',
    #  'nombre(s)',
    #  'escuela',
    #  'turno',
    #  'grado escolar',
    #  'grupo',
    #  'edad',
    #  'sexo',
    #  'version',
    #  'el_________ es una pelota de fuego',
    #  'a1',
    #  '__________ es una pelota de plata',
    #  'a2',
    #  'mi __________ es una pelota de pelos',
    #  'a3',
    #  'la frase pelota que canta tiene sentido?',
    #  'por que?',
    #  'a4s',
    #  'a4n',
    #  'explica lo que quiere decir mi hermanito es una pelota de gritos',
    #  'a5',
    #  'que otra cosa podria ser una pelota de pelos?',
    #  'por que?.1',
    #  'a6',
    #  'explica tu respuesta en la frase pelota de plata',
    #  'a7']

df = getCSV("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/Prueba 1/1_h_sec_todo_de_prueba1.csv")
a1 = colvals(df, 'el_________ es una pelota de fuego')
res = count(a1)
quickPlot(res['elements'],res['instances'], None)
