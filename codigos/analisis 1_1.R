library(readr)
library(dplyr)
library(tidytext)
library(Matrix)
library(ggplot2)

prueba <- read_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/Prueba 1/1_h_prim_todo_de_prueba1.csv')

#reactivo_uno_resp_uno, #reactivo_uno_resp_dos
resultados <- prueba %>%
  select(reactivo_tres) %>%
  count(reactivo_tres, sort = TRUE)
resultados

# Creaci???n de datos para la gr???fica
new_res <- subset(resultados, n!=1)
new_res_one <- subset(resultados, n == 1)
new_res
new_res_one

respuestas <- as.vector(new_res$reactivo_tres)

frecuencias <- as.vector(new_res$n)


p<-ggplot(data=new_res, aes(x=respuestas, y=frecuencias)) +
  geom_bar(stat="identity", fill = "steelblue") +
  geom_text(aes(label = frecuencias), vjust = -0.3, size = 3.5) + 
  theme_minimal()
p




