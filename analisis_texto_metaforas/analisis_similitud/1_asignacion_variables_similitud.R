getwd()
setwd("/misc/jasper/navarreten/analisis_texto_metaforas")
getwd()


rm(data)

data<-read.csv("similitudes_secundaria_3.csv")
View(data)

kruskal.test(data$puntaje_similitud~data$comparacion)

library(dunn.test)
dunn.test(data$puntaje_similitud,data$comparacion,method="bonferroni", list=T)

#comparaciones sin ceros (nan)

data1<-read.csv("similitudes_secundaria_4.csv")
View(data1)

kruskal.test(data1$puntaje_similitud~data1$comparacion)

dunn.test(data1$puntaje_similitud,data1$comparacion,method="bonferroni", list=T)


#variables

#Grupo solo secundaria
data2<-subset(data1,comparacion=="3_3")
#data2
#View(data2)

#Grupo solo hombres
data3<-subset(data1,comparacion=="3_2")
#data3
#View(data3)

#Grupo solo mujeres
data4<-subset(data1,comparacion=="3_1")
#data4
#View(data4)

#Grupo solo primaria hombres
data5<-subset(data1,comparacion=="3_0")
#data5
#View(data5)



#Summaries

sum_3_3<-summary(data2)
write.csv(sum_3_3, file ="sum_3_3.csv", row.names = F)

sum_3_2<-summary(data3)
write.csv(sum_3_2, file ="sum_3_2.csv", row.names = F)

sum_3_1<-summary(data4)
write.csv(sum_3_1, file ="sum_3_1.csv", row.names = F)

sum_3_0<-summary(data5)
write.csv(sum_3_0, file ="sum_3_0.csv", row.names = F)
