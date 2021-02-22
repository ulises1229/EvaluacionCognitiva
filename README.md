# EvaluacionCognitiva
Repositorio sobre:

* **El Estudio de la conectividad funcional cerebral asociada a la comprensión del lenguaje pragmático a través del desarrollo de la infancia a la adolescencia.

* **Proyecto de investigación sobre similitud de palabras.



## Estructura del repositorio

* **análisis corpus** - Contiene análisis estadísticos del rendimiento de corpus y bibliotecas de NLP (SpaCy, Word2Vec y Gensim)
* **analisis_texto_metaforas** - Contiene resultados y datos de análisis de similitud y conteo de palabras.
* **Bases de datos** - Contiene todos los csvs, tiene las bases de datos originales de las respuestas
* **codigos** - Contiene todos los Jupyter Notebooks y códigos usados en el procesamiento de los datos
* **comparación w2v y lsi** - Contiene gráficas, test estadísticos, post-hoc dunn y resumenes de la comparación entre Word2Vec y LSI (Latent Semantic Analysis).
* **cuenta_de_palabras** - Contiene csv's de conteo de palabras con clasificación **por reactivo** para todos los hombres y todas las mujeres, tests de primaria mujeres vs secundaria hombres y comparaciones entre niveles (Secundaria vs Primaria) y sexos (Hombres vs Mujeres).
* **FreqDistResp** - Contiene un csv con los resultados de la distribución de frecuencia de sustantivos, verbos, adjetivos y adverbios de los reactivos respondidos con texto
* **MASTER_ROWS** - Contiene las respuestas maestras y esclavas y una distribución de frecuencia de los reactivos respondidos con texto
* **Sin uso** - Contiene el proyecto original intacto como lo tenía Edna al principio





## análisis corpus 

***Comparaciones utilizando los siguientes corpus y bibliotecas de NLP:***
* Gensim
* Word2Vec
* SpaCy

***Descripción***
Se toman en cuenta las evaluaciones realizadas de forma manual, realizada por personas, para realizar comparaciones entre los diferentes puntajes
obtenidos utilizando las bibliotecas antes mencionadas. Se tomaron en cuenta las siguientes oraciones **base** para realizar las comparaciones.

* Pelota de gritos.
* Pelota de pelos.
* Pelota de plata.

En cada directorio se encuentran 3 contenidos:
* Análisis estadístico **Kruskal** de los datos contenidos en la columna.
* **Boxplot** de las diferencias entre evaluaciones.
* Post-hoc **dunn** para realizar comparaciones.

**Contenido:**
* tests_gensim_pelota_gritos 
* tests_gensim_pelota_pelos 
* tests_gensim_pelota_plata 
* tests_spacy_pelota_gritos 
* tests_spacy_pelota_pelos 
* tests_spacy_pelota_plata 
* tests_w2v_pelota_pelos 
* tests_w2v_pelota_pelos 
* tests_w2v_pelota_plata 






## analisis_texto_metaforas 

***Análisis de conteo de palabras y similitud de palabras hechos por Edna y Alejandro***

***Descripción***
En cada directorio se encuentran resultados y datos de análisis de similitud y conteo de palabras.

Los directorios "analisis_conteo_palabras" y "analisis_similitud" fueron realizados por Edna mientras que "analisis_conteo_alejandro" fue hecho por Alejandro.

**Contenido:**
* analisis_conteo_alejandro
    - tests **Tests estadísticos de conteo de palabras de niños y niñas de secundaria y primaria**
        - diferencias
        - normalidad
        - homogeneidad
        - conteo_clasif_ps_hm_mod.csv
    - tests_gensim **Tests estadísticos de resultados de similitud de palabras con gensim**
        - diferencias
        - normalidad
        - homogeneidad
        - graficas
        - resultados_gens.csv
* analisis_conteo_palabras
    - datos
    - resultados
    - 1_asignacion_variables_conteopalabras.R
    - 2_analisis_conteopalabras.R
    - exp_1.txt
    - exp1.docx
* analisis_similitud
    - datos
    - resultados
    - 1_asignacion_variables_similitud.R
    - 3_graficas_similitud.R







##### listado_archivos

doc





## Bases de datos 

***Contiene todos los csvs, tiene las bases de datos originales de las respuestas***



##### Primaria

* Sin uso - Contiene varios xlsx de la información de la BD original dividida por sexo (NO utilizar)
* conteo_primaria_general
    * Contiene el conteo de **todas las palabras** que usaron en los reactivos niños y niñas de primaria. 
* conteo_primaria_hombres
    * Contiene el conteo de **todas las palabras** que usaron los niños de primaria.
* conteo_primaria_mujeres
    * Contiene el conteo de **todas las palabras** que usaron los niños de primaria.
* palabras_corregidas_primaria
    * Contiene todas las columnas con respuestas en texto, limpias y con acentos de primaria.
* PRIMARIA_HOMBRES
    * Contiene **toda la información** filtrada a sólo niños de primaria.
* PRIMARIA_MUJERES
    * Contiene **toda la información** filtrada a sólo niños de primaria.
* PRIMARIA_TODO
    * Contiene toda la información de los resultados de niños y niñas de primaria.



##### Secundaria

* Sin uso - Contiene varios xlsx de la información de la BD original dividida por sexo (NO utilizar)

* Conceptos_Prueba2

    * ISASI

* Conceptos_Prueba3

    * ISASI

* conteo_secundaria_general

    * Contiene el conteo de **todas las palabras** que usaron en los reactivos niños y niñas de secundaria.

* conteo_secundaria_hombres

    * Contiene el conteo de **todas las palabras** que usaron los niños de primaria.

* conteo_secundaria_mujeres

    * Contiene el conteo de **todas las palabras** que usaron los niños de primaria.

* palabras_corregidas_secundaria

    * Contiene todas las columnas con respuestas en texto, limpias y con acentos de secundaria

* SECU_TODO_CLEAN

    * Contiene toda la información limpia de los resultados de niños de secundaria

* SECUNDARIA_PRUEBA2

    * Contiene toda la información de la prueba 2 limpia de los resultados de niños de secundaria

* SECUNDARIA_PRUEBA3

    * Contiene toda la información de la prueba 3 limpia de los resultados de niños de secundaria

    

##### Sin uso

* XLSX Originales - Contiene varios xlsx de la información de la BD original dividida por sexo (NO utilizar)

* escrito_edna_navarrete - Contiene la explicación y presentación del proyecto, objetivos y alcances

* metas_6 - zip con el proyecto original por Edna



##### resultados_similitudes_secundaria

Resultados de una prueba de similitud de una respuesta maestra del reactivo *explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_gritos* de 3_3, 3_2, 3_1, 3_0, 2_2, 2_1, 2_0, 1_1, 1_0, 0_0 con y sin stopwords





## codigos 

***Contiene todos los Jupyter Notebooks y códigos usados en el procesamiento de los datos***



##### .vscode y ______pycache______ - Carpetas con complementos de python, no tocar

##### JupyterNotebooks

* .ipynb_checkpoints - Carpetas con complementos de python, no tocar
*  modelo_personalizado
    * 
* ModelosStandard
    * 
* FreqDist Respuestas
    * 
* Similitud Gensim
    * 
* Similitud NLTK
    * 
* Similitud Notebook
    * 

##### Clasificador

* Utilizando la librería SpaCy para NLP, clasifica en: verbos, adjetivos, sustantivos y adverbios las palabras contenidas en un CSV y hace un conteo de las palabras clasificadas para posteriormente dividir el conteo en un CSV para cada tipo de palabras dando un total de 4.

**Nota importante:** Para utilizar este script es necesario haber hecho una limpieza y corrección previa de las palabras que se pretenden clasificar y posteriormente contar de lo contrario puede derivarse esto en resultados inexactos.

##### conceptoSelector

* Obtiene todos los conceptos y dominios fuente de todas las respuestas a todos los reactivos, y los exporta en un csv. Tanto para prueba 2 como prueba 3. La estructura del csv es la siguiente:

  cx_frase  concepto_r_x  df_x  c1_x  c2_x  c3_x  criterio_x

  Donde x es el reactivo

##### conteo_clasif_palabras

* Analiza cada celda de un csv, busca si existe una falta de ortografía o gramática en la celda actual del recorrido y da diferentes sugerencias para corregir esa falta utilizando el wrapper de la librería Hunspell (CyHunspell). Una vez corregida se almacena en un diccionario y en caso de que exista una falla parecida a esa la corregirá automáticamente y avanzará a la siguiente celda.

##### conteo_palabras

* Hace un recorrido por cada fila deseada de un CSV, hace un conteo de las palabras que existan en cada celda omitiendo las celdas que contengan los siguientes valores:
"NS", "0", "NN", "WW" y "-" sustituyéndolos con "0", suma todo de cada fila y los valores resultantes los almacena en un dataframe para después ser convertido en CSV.

##### csvCleaner

* Codigo para limpiar un csv, hace un trim a todas las celdas y reduce todos los espacios entre palabras a 1

##### formatter

* Usando la librería SpaCy, formatea las palabras proporcionadas para ser clasificadas sin importar el contexto que pueda modificar el tipo de palabra.

Este script se usa especialmente para clasificar palabras en verbos o adjetivos pero que son identificados como auxiliares por SpaCy. Este formateador se usa previo a trainer.py.

#### testing_good
Script que hace los siguientes análisis estadísticos y los almacena en csv's junto con gráficas de caja (boxplots) para representar diferencias entre grupos.

**Normalidad:**
    - Jarque Test.
    - Anderson Test.
    - Shapiro-wilk Test.
    - Shapiro-francia Test.
    - Pearson Test.
    - Kolmogorov Test.

**Homogeneidad:**
    - Bartlett Test.
    - Levene Test.

**Diferencias de varianza:**
    - Wilcox (U de Mann-Whitney).
    - Kruskal Test.

#### testing 2.0v
* Versión actualizada de testing_good que permite crear sub-dataframes para análisis más específicos.


#### multi_testing
Actualización de testing_good y Testing2.0 con mayor automatización.

**Cómo usar:**

Código...


##### new_corrector

* 

##### oraciones_propn

* 

##### palabras_propn

* 

##### quickPlotter

* Genera una freqdist de los sustantivos, verbos, adverbios y adjetivos de todo un csv

##### similitud

* Hace una evaluacion simple de similitud entre todas las columnas con respuestas evaluadas con menos de 3 con

  respuestas evaluadas con 3, el metodo es el siguiente:

  

  frase 1: la mujer corre

  frase 2: el hombre salta

  

  El algoritmo de similitud compara cada token con cada token y retorna una evaluacion numerica entre 0 y 1 basada

  en el diccionario de vectores que importamos:

  

  la  -> el   -> 0.9

  la  -> hombre -> 0.3

  la  -> salta -> 0.1

  

  mujer -> el   -> 0.5

  mujer -> hombre -> 0.7

  mujer -> salta -> 0.1

  

  corre -> el   -> 0.1

  corre -> hombre -> 0.2

  corre -> salta -> 0.6

  

  Y para encontrar la similitud entre oraciones se calcula un promedio de estas comparaciones:

  

  0.9 + 0.3 + 0.1 + 0.5 + 0.7 + 0.1 + 0.1 + 0.2 + 0.6 / 9 = 0.38

##### trainer

* Después de utilizar formatter.py se utiliza este código para utilizar las oraciones con sus tags pre establecidos para crear un modelo desde 0 de SpaCy que pueda ser utilizado posteriormente.



## comparación w2v y lsi 

***Contiene gráficas, test estadísticos, post-hoc dunn y resumenes de la comparación entre Word2Vec y LSI (Latent Semantic Analysis).***

* Oraciones utilizadas como base para probar los dos algoritmos:
    - Que mi hermanito es muy griton y esta gordito.
    - Que mi hermanito grita mucho.

* boxplot's - que mi hermanito es muy grito y esta gordito
* boxplot's - que mi hermanito grita mucho
* csv's con resultados de lsi de Mario
* diferencias
* normalidad
* Pruebas de Dunn
* resumenes
* res_generales.csv



##### listado_archivos

doc





## cuenta_de_palabras 

***Breve_explicación_del_folder***



##### listado_archivos

doc





## FreqDistResp 

***Contiene un csv con los resultados de la distribución de frecuencia de sustantivos, verbos, adjetivos y adverbios de los reactivos respondidos con texto***





## MASTER_ROWS 

***Contiene las respuestas maestras y esclavas y una distribución de frecuencia de los reactivos respondidos con texto***



##### PRUEBA_1 - Contiene las master rows y sus instancias de los reactivos con texto de la prueba 1

##### PRUEBA_2 - Contiene las master rows y sus instancias de los reactivos con texto de la prueba 2

##### PRUEBA_3 - Contiene las master rows y sus instancias de los reactivos con texto de la prueba 3

##### Freq_Dist_Prueba_3 - Contiene las master rows, sus instancias y conteos de los reactivos con texto de la prueba 3





## Sin uso 

***Contiene el proyecto original intacto como lo tenía Edna al principio***

##### modificados - contiene algunos archivos de pruebas de código y modificaciones en las bases de datos (xlsx o csv)

##### originales - el proyecto intacto

