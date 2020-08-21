getwd()
setwd("/media/pinker/KINGSTON/tidytext")
setwd("E:/tidytext")
getwd()

#install.packages("readr")

library(readr)

data5 <- read.csv('5.csv', header = T)
#Necesito encontrar la forma de leer excel sin cambiarlo a csv, porque cuando se cambia a
#.csv, todos los caracetres especiales se cambian y se ponen signos raros y asi ya no 
#puedo cambiar nada
data5 <- read.table('5.xlsx')
View(data5)

colnames(data5)
str(data5)

#install.packages("tidyverse")

library(tidyverse)
library(tidyr)
library(dplyr)

data5.1 <- str_replace_all(data5, "?","n")
View(data5.1)

library (stringr)




#Esto es un experimento con los ejemplos de la ayuda de r para str_replace,
#para ver que hace con cada instruccion

fruits <- c("one apple", "two pears", "three bananas")
fruits
str_replace(fruits, "[aeiou]", "-")
str_replace_all(fruits, "[aeiou]", "-")
str_replace_all(fruits, "[aeiou]", toupper)
str_replace_all(fruits, "b", NA_character_)
str_replace_all(fruits, "a", NA_character_)
str_replace_all(fruits, "o", NA_character_)

str_replace(fruits, "([aeiou])", "")
str_replace(fruits, "([aeiou])", "\\1\\1")
str_replace(fruits, "[aeiou]", c("1", "2", "3"))
str_replace(fruits, c("a", "e", "i"), "-")

#Esta está mal
str_replace_all(fruits, c("one" = "1", "two" = "2", "three" = "3"))

#Intento quitar acentos facilmente
fruits2 <- c("one  ápple", "twó  péars", "thrée  bananas")
fruits2
str_replace_all(fruits2, c("á" = "a", "é"= "e", "ó"= "o"))

str_replace_all(fruits2,"  "," ")
