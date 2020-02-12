library(readr)
library(dplyr)
library(tidytext)
library(Matrix)
library(ggplot2)

prueba <- read_csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/Bases de datos/Primaria/Prueba 1/1_h_prim_todo_de_prueba1.csv')
resultados <- prueba %>%
  select(reactivouno) %>%
  count(reactivouno, sort = TRUE)
resultados

# Creaci�n de datos para la gr�fica
M <- as.vector(resultados$reactivouno) #valores de los resultados
H <- as.vector(resultados$n) #veces en las que se repiten los resultados
print(H)
print(M)

p<-ggplot(data=resultados, aes(x=M, y=H, color = H)) +
  geom_bar(stat="identity", fill = "steelblue") +
  geom_text(aes(label = H), vjust = -0.3, size = 3.5) + 
  theme_minimal()
p
