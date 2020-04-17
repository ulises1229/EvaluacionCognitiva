library(readr)
library(dplyr)
library(tidytext)
library(Matrix)
library(ggplot2)

datos <- read.csv('C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/muestras_ttest.csv')

View(datos)

ggplot(datos, aes(calificacion, fill = estudios, color = estudios))+
  geom_density(alpha=0.2)+
  xlim(0,23)

qqnorm(datos$calificacion)
qqline(datos$calificacion, col="blue")

shapiro.test(datos$calificacion)

ggplot(datos, aes(estudios, calificacion, fill = estudios, color = estudios))+
  geom_boxplot(alpha=0.4)+
  theme(legend.position = "none")

datos %>%
  group_by(estudios) %>%
  summarize(total = n(),
            promedio_calificaciones = mean(calificacion))

var.test(calificacion ~ estudios, data = datos)

t.test(calificacion ~ estudios, data = datos, var.equal = T)