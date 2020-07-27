library(ggplot2)
library(dplyr)
library(moments)
library(nortest)
library(lawstat)
#quit(save="default", status = 0, runLast = TRUE)

rm(list = ls())
getwd()
setwd('C:/Users/Alex Isasi/Documents/analisis_conteo_palabras/analisis_conteo_alejandro')
source('Testing.R')
data = read.csv('conteo_clasif_ps_hm_mod.csv')

#View(data)

#Test de normalidad
print('Comenzando test de normalidad')
#dataframe <- data[,4:13]
#dataframe

#test_tags <- c("norm", "vars", "difs_sex", "difs_niv", "difs_grup", "dunn", )
#for t in test_tags:
  #testing(data)

testing(data)



