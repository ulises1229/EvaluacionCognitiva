
rm(list = ls())
library(ggplot2)
library(dplyr)
library(moments)
library(nortest)
library(lawstat)
#quit(save="default", status = 0, runLast = TRUE)

setwd("C:/Users/Alex Isasi/Documents/analisis_conteo_palabras/analisis_conteo_alejandro")

source('testing_good.R')
data = read.csv('conteo_clasif_ps_hm_mod.csv') 

tests <- c('normalidad', 'varianzas', 'diferencias')
first_link <- paste0(getwd(),'/tests')

if(!dir.exists(first_link)){
  dir.create(first_link)
}

for(test in tests){
  setwd(first_link)
  testing(data, test)
}



