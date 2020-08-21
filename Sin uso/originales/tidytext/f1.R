rm(list= ls())

source("analisis_item.R")

for (i in 1:7){
analisis_item("a_hm_p.csv",i)}

#analisis_item("datos_limpios/mujeres/10.csv",4)
