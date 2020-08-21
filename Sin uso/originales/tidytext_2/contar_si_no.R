getwd()
setwd("E:/tidytext_2/")
getwd()

rm(data1)
#data<-read.csv("E:/metas_6/3_hm_ps_var_6.csv")
data<-read.csv("contar_si_no_hm_p.csv")
View(data)


data1<-subset(data,Es.Posible=="no")
#data1
View(data1)

data2<-subset(data,Es.Posible=="si")
#data1
View(data2)

levels(data1$Cal_1_m)

as.factor(data1$Cal_1_m)

sum(data1$Cal_1_m==0)
sum(data1$Cal_1_m==1)
sum(data1$Cal_1_m==2)
sum(data1$Cal_1_m==3)

sum(data2$Cal_1_m==0)
sum(data2$Cal_1_m==1)
sum(data2$Cal_1_m==2)
sum(data2$Cal_1_m==3)


data3<-subset(data,Es.Posible.1=="no")
#data1
View(data3)

data4<-subset(data,Es.Posible.1=="si")
#data1
View(data4)

sum(data3$Cal_1_m==0)
sum(data3$Cal_1_m==1)
sum(data3$Cal_1_m==2)
sum(data3$Cal_1_m==3)

sum(data4$Cal_1_m==0)
sum(data4$Cal_1_m==1)
sum(data4$Cal_1_m==2)
sum(data4$Cal_1_m==3)

data5<-subset(data,Es.Posible.2=="no")
#data1
View(data5)

data6<-subset(data,Es.Posible.2=="si")
#data1
View(data6)

sum(data5$Cal_1_m==0)
sum(data5$Cal_1_m==1)
sum(data5$Cal_1_m==2)
sum(data5$Cal_1_m==3)

sum(data6$Cal_1_m==0)
sum(data6$Cal_1_m==1)
sum(data6$Cal_1_m==2)
sum(data6$Cal_1_m==3)








