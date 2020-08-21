rm(list= ls())

#source("/media/pinker/KINGSTON/tidytext_2/analisis_item.R")
source("E:/tidytext_2/analisis_item.R")

for (i in 1:27){
  analisis_item("E:/tidytext_2/datos_limpios/a_hm_s.csv",i)}

#analisis_item("/media/pinker/KINGSTON/tidytext_2/datos_limpios/a_hm_s.csv",i)}

#analisis_item("datos_limpios/mujeres/10.csv",4)
