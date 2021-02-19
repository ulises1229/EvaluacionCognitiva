
rm(list = ls())
library(ggplot2)
library(dplyr)
library(tidyr)
library(moments)
library(nortest)
library(lawstat)


setwd("C:/Users/Alex Isasi/Documents/analisis_conteo_palabras/analisis_conteo_alejandro")

source('testing_good.R')
data = read.csv('resultados_gens.csv', na.strings = c("", "NA")) 

tests <- c('normalidad', 'varianzas', 'diferencias')
first_link <- paste0(getwd(),'/tests_gensim')

if(!dir.exists(first_link)){
  dir.create(first_link)
}

for(test in tests){
  setwd(first_link)
  testing(data, test)
}



