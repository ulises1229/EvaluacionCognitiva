getwd()
setwd("/misc/jasper/navarreten/analisis_texto_metaforas")
getwd()

source("1_asignacion_variables_conteopalabras.R")

#datos descriptivos de cada grupo

sum_todo<-summary(data)
write.csv(sum_todo, file ="sum_todo.csv", row.names = F)

sum_solo_primaria<-summary(data1)
write.csv(norm_solo_primaria, file ="norm_solo_primaria.csv", row.names = F)

sum_solo_secundaria<-summary(data2)
write.csv(sum_solo_secundaria, file ="sum_solo_secundaria.csv", row.names = F)

sum_solo_hombres<-summary(data3)
write.csv(sum_solo_hombres, file ="sum_solo_hombres.csv", row.names = F)

sum_solo_mujeres<-summary(data4)
write.csv(sum_solo_mujeres, file ="sum_solo_mujeres.csv", row.names = F)

sum_solo_primaria_hombres<-summary(data5)
write.csv(sum_solo_primaria_hombres, file ="sum_solo_primaria_hombres.csv", row.names = F)

sum_solo_primaria_mujeres<-summary(data6)
write.csv(sum_solo_primaria_mujeres, file ="sum_solo_primaria_mujeres.csv", row.names = F)

sum_solo_secundaria_hombres<-summary(data7)
write.csv(sum_solo_secundaria_hombres, file ="sum_solo_secundaria_hombres.csv", row.names = F)

sum_solo_secundaria_mujeres<-summary(data8)
write.csv(sum_solo_secundaria_mujeres, file ="sum_solo_secundaria_mujeres.csv", row.names = F)


#normalidad de cada grupo con prueba de  normalidad shapiro wilk

norm_<-shapiro.test(data$total_palabras)
norm_solo_primaria<-shapiro.test(data1$total_palabras)
norm_solo_secundaria<-shapiro.test(data2$total_palabras)
norm_solo_hombres<-shapiro.test(data3$total_palabras)
norm_solo_mujeres<-shapiro.test(data4$total_palabras)
norm_solo_primaria_hombres<-shapiro.test(data5$total_palabras)
norm_solo_primaria_mujeres<-shapiro.test(data6$total_palabras)
norm_solo_secundaria_hombres<-shapiro.test(data7$total_palabras)
norm_solo_secundaria_mujeres<-shapiro.test(data8$total_palabras)

grupos<-c("todo","solo_primaria","solo_secundaria","solo_hombres","solo_mujeres","solo_primaria_hombres",
          "solo_primaria_mujeres","solo_secundaria_hombres","solo_secundaria_mujeres")

norm_estadistico_w<-c(norm_todo$statistic,norm_solo_primaria$statistic,norm_solo_secundaria$statistic,
                      norm_solo_hombres$statistic,norm_solo_mujeres$statistic,norm_solo_primaria_hombres$statistic,
                      norm_solo_primaria_mujeres$statistic,norm_solo_secundaria_hombres$statistic,
                      norm_solo_secundaria_mujeres$statistic)

norm_pvalor<-c(norm_todo$p.value,norm_solo_primaria$p.value,norm_solo_secundaria$p.value,
               norm_solo_hombres$p.value,norm_solo_mujeres$p.value,norm_solo_primaria_hombres$p.value,
               norm_solo_primaria_mujeres$p.value,norm_solo_secundaria_hombres$p.value,
               norm_solo_secundaria_mujeres$p.value)

prueba_normalidad_shapiro_wilk<-data.frame(grupos,norm_estadistico_w,norm_pvalor)

write.csv(prueba_normalidad_shapiro_wilk,file="prueba_normalidad_shapiro_wilk.csv",row.names = F)


#Prueba de homogeneidad de varianzas

var.test(data$total_palabras,data$nivel)
var.test(data$total_palabras~data$sexo)

bartlett.test(data$total_palabras,data$nivel)
bartlett.test(data$total_palabras~data$sexo)


#Prueba u.de mann whitney, diferencias entre las medianas

diferencias_total_hombres_mujeres<-wilcox.test(data$total_palabras~data$sexo)
diferencias_hombres_primaria_vs_hombres_secundaria<-wilcox.test(data3$total_palabras~data3$nivel)
diferencias_mujeres_primaria_vs_mujeres_secundaria<-wilcox.test(data4$total_palabras~data4$nivel)
diferencias_hombres_vs_mujeres_primaria<-wilcox.test(data1$total_palabras~data1$sexo)
diferencias_hombres_vs_mujeres_secundaria<-wilcox.test(data2$total_palabras~data2$sexo)
diferencias_total_primaria_secundaria<-wilcox.test(data$total_palabras~data$nivel)

#Graficas diferencias entre grupos

library (ggplot2)
library(scales)

#Boxplot diferencia entre hombres y mujeres (primaria y secundaria juntos)

ggplot(data, aes(x=as.factor(sexo),y=(total_palabras), fill=as.factor(sexo))) + 
  geom_boxplot(alpha=0.2, notch = T) + 
  labs(title = "Diferencias entre Sexos Total")+
  ylab("Numero total de palabras")+
  xlab("Sexo")+
  scale_fill_brewer(palette = "Set1") +
  theme_minimal()

ggsave("diferencias_genero.jpeg")


#Boxplot diferencia entre hombres primaria y hombres secundaria)

ggplot(data3, aes(x=as.factor(nivel),y=(total_palabras), fill=as.factor(nivel))) + 
  geom_boxplot(alpha=0.2, notch = T) + 
  labs(title = "Diferencias entre hombres primaria y hombres secundaria")+
  ylab("Numero total de palabras")+
  xlab("Nivel Escolar")+
  scale_fill_brewer(palette = "Set2") +
  theme_minimal()

ggsave("diferencias_hombres_primaria_vs_hombres_secundaria.jpeg")


#Boxplot diferencia entre mujeres primaria y mujeres secundaria)

ggplot(data4, aes(x=as.factor(nivel),y=(total_palabras), fill=as.factor(nivel))) + 
  geom_boxplot(alpha=0.2, notch = T) + 
  labs(title = "Diferencias entre mujeres primaria y mujeres secundaria")+
  ylab("Numero total de palabras")+
  xlab("Nivel Escolar")+
  scale_fill_brewer(palette = "Set3") +
  theme_minimal()

ggsave("diferencias_mujeres_primaria_vs_mujeres_secundaria.jpeg")