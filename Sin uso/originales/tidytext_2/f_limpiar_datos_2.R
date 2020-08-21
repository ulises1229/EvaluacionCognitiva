limpiar_datos <- function (fileN, item){

  item_1 <-c()
  item_2 <-c()
  item_3 <-c()
  item_4 <-c()
  item_5 <-c()
  item_6 <-c()
  item_7 <-c()
  item_8 <-c()
  
 library(readxl)
  
  data5 <- read_xlsx(fileN)
  View(data5)
  
  #Explorar datos
  colnames(data5)
  str(data5)
  
  data5.1 <-as.data.frame(data5)
  View(data5.1)
  str(data5.1)
  attributes(data5.1)
  is.atomic(data5.1)

for (i in 1:9)  
#
  data5.1.5 <- data5.1[,item]
  attributes(data5.1.5)
  View (data5.1.5)
  str(data5.1.5)
  is.atomic(data5.1.5)
  
  library(stringr)
  
  data5.2.5 <- str_replace_all(data5.1.5, "ñ","n")
  data5.2.5
 
  data5.2.6 <- str_replace_all(data5.2.5, c("á"= "a", "é"= "e","í"= "i", "ó"= "o", "ú"= "u"))
  data5.2.6
  
  data5.2.7 <- str_replace_all(data5.2.6, c("à"= "a", "è"= "e","ì"= "i", "ò"= "o", "ù"= "u"))
  data5.2.7
  data5.2.8 <- str_replace_all(data5.2.7, "  "," ")
  data5.2.8
  
  str(data5.2.8)
  
  nombre1 <- paste("item_",item, ".csv", sep="")
  write.csv(data5.2.8, nombre1, row.names = F)
  
  }

