import pandas as pd

"""
Codigo para limpiar un csv, hace un trim a todas las celdas y reduce todos los espacios entre palabras a 1
"""

# Un iterable para evaluar si existe algun espacio en el arreglo dado
def whitespaceInList(array):
    for x in array:
        if x != "":
            pass
        else:
            return True # si hay algun espacio en el arreglo
    return False # despues del recorrido, si no hay espacios en el arreglo


# Limpia todos los espacios a la izq o der y minimiza los espacios en medio a solo uno
def cleanWhitespace(string):
    string = string.strip()
    array = string.split(" ")
    # Se recorrera el arreglo de strs con espacios hasta que haya ninguno
    while(whitespaceInList(array)):
        for x in array:
            if x == "":
                array.remove(x)
    s = " ".join(array)
    return s


# Limpia un DataFrame de todo el whitespace que tenga y reduce todos los espacios entre palabras a 1
def cleanDataFrame(df):
    for column in df:
        for row in range(len(df)):
            # recorrido de todo el df por columna y fila
            text = df.at[row, column]
            try:
                if isinstance(text, str) == True:
                    clean_text = cleanWhitespace(text)
                    df.at[row, column] = clean_text
                elif isinstance(text, int) == True:
                    clean_text = cleanWhitespace(str(text))
                    clean_text = int(clean_text)
                    df.at[row, column] = clean_text
                else:
                    pass
            except:
                print("Error ocurred, type: " + type(text))
    return df


df = pd.read_csv("C:/Users/Drablaguna/Desktop/SECU_TODO_NEW.csv") # aqui ingresamos la ruta del csv
print("Limpiando CSV...\n")
df = cleanDataFrame(df)
df.to_csv("C:/Users/Drablaguna/Desktop/CLEAN.csv", index=False) # y la ruta de salida del csv limpio
print("\nCSV limpiado satisfactoriamente")
