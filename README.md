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

* 

##### conceptoSelector

* 

##### conteo_clasif_palabras

* 

##### conteo_palabras

* 

##### csvCleaner

* 

##### emotionAnalyzer

* 

##### formatter

* 

##### new_corrector

* 

##### oraciones_propn

* 

##### palabras_propn

* 

##### quickPlotter

* 

##### similitud

* 

##### trainer

* 





## comparación w2v y lsi 

***Breve_explicación_del_folder***



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

