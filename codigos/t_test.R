library(readr)
library(dplyr)
library(tidytext)
library(Matrix)
library(ggplot2)

rm(list = ls())
ruta <- 'C:/Users/Alex Isasi/Documents/GitHub/EvaluacionCognitiva/cuenta_de_palabras/Prueba t de cuenta de palabras/Hombres vs Mujeres_SECUNDARIA/'
datos <- read.csv(paste0(ruta,'SECU_HOM_MUJ_PALABRAS.csv'))
View(datos)

png(paste0(ruta,'grafica_densidad.png'), width = 800, height = 800, units = "px")
ggplot(datos, aes(suma_total, fill = genero, color = genero))+
  geom_density(alpha=0.2)+
  xlim(2,400)
dev.off()


png(paste0(ruta,'grafica_qq_normalidad.png'))
qqnorm(datos$suma_total)
qqline(datos$suma_total, col="blue")
dev.off()


sink(paste0(ruta,'test_shapiro_normalidad.txt'))
print(shapiro.test(datos$suma_total))
sink()

png(paste0(ruta,'grafica_boxplot.png'))
ggplot(datos, aes(genero, suma_total, fill = genero, color = genero))+
  geom_boxplot(alpha=0.4)+
  theme(legend.position = "none")
dev.off()

sink(paste0(ruta,'resumen_general.txt'))
print(summary(datos$suma_total))
sink()

sink(paste0(ruta,'test_de_varianza.txt'))
print(var.test(suma_total ~ genero, data = datos))
sink()

sink(paste0(ruta, 't_test.txt'))
print(t.test(suma_total ~ genero, data = datos, var.equal = T))
sink()
