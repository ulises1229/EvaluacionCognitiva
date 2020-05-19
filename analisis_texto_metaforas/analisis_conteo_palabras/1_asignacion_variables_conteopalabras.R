
getwd()
setwd("/misc/jasper/navarreten/analisis_texto_metaforas")
getwd()


rm(data)

data<-read.csv("conteo_palabras_todos.csv")
View(data)

#Grupo solo primaria
data1<-subset(data,nivel==1)
#data1
#View(data1)

#Grupo solo secundaria
data2<-subset(data,nivel==2)
#data2
#View(data2)

#Grupo solo hombres
data3<-subset(data,sexo=="M")
#data3
#View(data3)

#Grupo solo mujeres
data4<-subset(data,sexo=="F")
#data4
#View(data4)

#Grupo solo primaria hombres
data5<-subset(data,nivel==1 & sexo=="M")
#data5
View(data5)

#Grupo solo primaria mujeres
data6<-subset(data,nivel==1 & sexo=="F")
#data6
View(data6)

#Grupo solo secundaria hombres
data7<-subset(data,nivel==2 & sexo=="M")
#data7
View(data7)

#Grupo solo secundaria mujeres
data8<-subset(data,nivel==2 & sexo=="F")
#data8
View(data8)
