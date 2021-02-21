import pandas as pd

"""
Obtiene todos los conceptos y dominios fuente de todas las respuestas a todos los reactivos, y los exporta en un csv.
Tanto para prueba 2 como prueba 3

Lee como dataframe el csv de prueba 2 y 3
Extrae la info como dataframes y los concatena al final
La estructura final queda de la siguiente manera:

cx_frase    concepto_r_x    df_x    c1_x    c2_x    c3_x    criterio_x

Donde x es el reactivo

"""

# PRUEBA 2

# df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/SECUNDARIA_PRUEBA2.csv") # ingresamos la ruta del csv de prueba 2

# def get_df(df:object, idx:int, evl:int) -> object:
#     return df[[
#         f'c{idx}_frase',
#         f'concepto_r_{idx}',
#         f'df_{idx}',
#         f'c1_{idx}',
#         f'c2_{idx}',
#         f'c3_{idx}',
#         f'criterio_{idx}',
#         f'c{idx}']
#     ].loc[df[f'c{idx}']==evl]

# dfs = []

# for i in range(1,19):
#     print(f"---> Getting data of {df[f'c{i}_frase'][0]}")
#     df_3 = get_df(df,i,3)
#     df_2 = get_df(df,i,2)
#     df_1 = get_df(df,i,1)
#     df_col = pd.concat([df_3,df_2,df_1])
#     dfs.append(df_col)

# final_df = pd.concat(dfs)

# final_df.to_csv("C:/Users/Drablaguna/Desktop/Conceptos_Prueba2.csv",encoding='latin1') # aqui ingresamos la ruta para exportar el csv




# PRUEBA 3

df = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/SECUNDARIA_PRUEBA3.csv") # ingresamos la ruta del csv de prueba 3

def get_df(df:object, idx:int, evl:int) -> object:
    return df[[
        f'b{i}_frase',
        f'b{i}_tipo',
        f'b{i}_ruta',
        f'c1_b{i}',
        f'c2_b{i}',
        f'c3_b{i}',
        f'c4_b{i}',
        f'b{i}']
    ].loc[df[f'b{idx}']==evl]

dfs = []

for i in range(1,28):
    print(f"---> Getting data of {df[f'b{i}_frase'][0]}")
    df_3 = get_df(df,i,3)
    df_2 = get_df(df,i,2)
    df_1 = get_df(df,i,1)
    df_col = pd.concat([df_3,df_2,df_1])
    dfs.append(df_col)

final_df = pd.concat(dfs)

final_df.to_csv("C:/Users/Drablaguna/Desktop/Conceptos_Prueba3.csv",encoding='latin1') # aqui ingresamos la ruta para exportar el csv

