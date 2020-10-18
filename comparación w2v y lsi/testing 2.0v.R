#Testing v2.0
#Este script calcula con base los datos que sean ingresados y lo que se desee las siguientes pruebas estadísticas:
#Para normalidad. Jarque test, Anderson test, kolmogorov, pearson, shapiro-francia, shapiro-wilk
#Para homogeneidad de varianzas. Bartlett test, Levene test
#Para diferencia de varianzas(dependiendo de los datos ingresados Wilcox test/U de Mann Whitney, kruskal wallis, Friedman test
#Borrado de variables existentes
rm(list = ls())

#Librerias
library(ggplot2)
library(stats)
library(dplyr)
library(tidyr)
library(moments)
library(nortest)
library(lawstat)
library(ggthemes)

get_names <- function(type) { #Función que retorna la columna con tipos de test deseados dependiendo del tipo que ingrese a la función
  vec_tot_of_names <- c()
  if(type == 'normalidad'){ test_names <- list('jarque','anderson', 'kolmogorov', 'pearson', 'shapfran', 'shapwilk')}
  if (type == 'homogeneidad') { test_names <- list('bartlett', 'levene')} #levene
  if (type == 'diferencias') { test_names <- list('kruskal')} #wilcox, kruskal, friedman
  for(t in test_names){
    vec_of_names <- paste0(t, c('_estadistico', '_pvalor', '_conclusion'))
    vec_tot_of_names <- c(vec_tot_of_names, vec_of_names)
  }
  return(vec_tot_of_names)
}

#Función que organiza dataframes en directorios y los guarda como CSV's
organizer <- function(list_dataframes, type = 'diferencias_'){
  x = 1
  for(df in list_dataframes){
    if(!dir.exists(type)){
      dir.create(type)
    }
    setwd(type)
    write.csv(df, file = paste0(names(list_dataframes[x]),'.csv')) #ejemplo: normalidad_todo, diferencias_ph_vs_pm.csv
    x = x + 1
    setwd(first_link)
  }
}

#Función que retorna la columna de resultados dependiendo de la columna analizada y el test ejecutado
get_column <- function(list_of_tests){
  column <- c()
  for(test in list_of_tests){
    new_data <- c(test$statistic, test$p.value, get_conclusion(test$p.value))
    column <- c(column, new_data)
  }
  return(column)
}

#Agregar a esta función el tiepo de test para que devuelva cadena dependiendo del tipo
get_conclusion <- function(pvalor){ 
  if(pvalor <= 0.05){
    return('Rechaza la hipótesis nula')
  } else{
    return('No rechaza la hipotesis nula')
  }
}


#Función que grafica diferencias por cada subdf con boxplots
get_plot <- function(subdf, gp, i){
  rango <- max(subdf[i], na.rm = T)
  column = names(subdf)
  themes = c("PuBu", "GnBu", "OrRd", "YlGn", "PuRd", "BuPu", "Dark2", "YlOrBr")
  View(subdf)
  print(gp)
  print(subdf[1, divider])
  print(column[i])
  
   pl <- ggplot(subdf, aes_string(x=gp, y=column[i], group=gp, fill = as.factor(gp))) +
     geom_boxplot() +
     geom_jitter(shape=16, position=position_jitter(0.2)) +
     scale_y_continuous(breaks = seq(0,rango,2)) +
     scale_fill_brewer(palette = sample(themes,1)) +
     ggtitle(paste0("Diferencias entre: ", gp,". De: ", column[i],". En: ",divider, ": ", subdf[1, divider])) + 
     labs(x = "grupos", y = "Frecuencia") +
   ggsave(paste0("boxplot_por_",gp,"_",column[i],"_en_",divider,"_",subdf[1, divider],".jpeg")) 
   print(pl)

}

testing_homogeneity <- function(variable, group){
  column <- c()
  list_of_tests <- list(bartlett.test(variable~group), #bartlett
                levene.test(variable, group)) #levene
  
  col <- get_column(list_of_tests)
  return(col)
}

testing_difference <- function(variable, group, sub){
  list_of_tests <- list(kruskal.test(variable ~ group)) #wilcox
  column <- get_column(list_of_tests)
  
  return(column)
}

testing_normality <- function(variable){
  
 list_of_tests <- list(jarque.test(variable), #jarque
               ad.test(variable),     #anderson
               lillie.test(variable), #kolmogorov
               pearson.test(variable), #pearson
               sf.test(variable),     #shapiro-francia
               shapiro.test(variable)) #shapiro-wilk
 
 col <- get_column(list_of_tests)
 return(col)
}

Testing <- function(){ 
  for(i in cols_to_analyze){
    var_cols <- as.vector(unlist(data[i]))
    group <- as.vector(unlist(data["eval_og"]))
    print(var_cols)
    print(group)
    #new_col_norm <- testing_normality(var_cols)
    #df_normalidad <- cbind(df_normalidad, new_col_norm)
    #new_col_homo <- testing_homogeneity(var_cols, group)
    #df_homogeneidad <- cbind(df_homogeneidad, new_col_homo)
    new_col_diff <- testing_difference(var_cols, group)
    df_diferencias_1 <- cbind(df_diferencias_1, new_col_diff)
    
    #sub = 1
    #for(subdf in subdfs){ #itera por cada columna 
    #  get_plot(subdf, grupo, i)
      
    #  var_cols <- as.vector(unlist(subdf[i]))
    #  group <- as.vector(unlist(subdf[grupo]))
      
    #  new_col_diff <- testing_difference(var_cols, group, sub)
     
    #  if(sub == 1){ #para el primer subdf
    #    df_diferencias_1 <- cbind(df_diferencias_1, new_col_diff)
    #  } else if(sub == 2){ #para el segundo subdf
    #    df_diferencias_2 <- cbind(df_diferencias_2, new_col_diff)
    #  }
    #  sub = sub + 1
    #}
  }
  #print(df_normalidad)
  
  #names(df_normalidad)[2:7] <- names(data)[cols_to_analyze]
  #names(df_homogeneidad)[2:8] <- names(data)[cols_to_analyze]
  names(df_diferencias_1)[2:7] <- names(data)[cols_to_analyze]
  #names(df_diferencias_2)[2:8] <- names(data)[cols_to_analyze]
  list_of_dataframes <- list(df_diferencias_1 = df_diferencias_1) #df_normalidad, df_homogeneidad df_diferencias_2
  organizer(list_of_dataframes)
}

#Main
setwd('C:\\Users\\Alex Isasi\\Documents\\analisis_conteo_palabras\\analisis_conteo_alejandro') #carpeta de trabajo
data = read.csv('res_generales.csv', na.strings = c("", "NA")) #Ingresar csv con muestras #conteo_clasif_ps_hm_mod.csv
#df_normalidad <- data.frame(tests = get_names('normalidad')) #dataframe de normalidad
#df_homogeneidad <- data.frame(tests = get_names('homogeneidad')) #dataframe de homogeneidad de varianzas
df_diferencias_1 <- data.frame(tests = get_names('diferencias')) #dataframe 1 de diferencia de varianzas
#df_diferencias_2 <- data.frame(tests = get_names('diferencias')) #dataframe 2 de diferencia de varianzas
first_link <- paste0(getwd(),'/eficiencia de datos') #creación de primer carpeta

if(!dir.exists(first_link)){
  dir.create(first_link)
} 

setwd(first_link)
cols_to_analyze <- 3:8 #Seleccionar columnas a tomar en cuenta como variables
#datos para diferencia de varianzas
#divider = "sexo"
#grupo = "nivel" #Grupo para dividir dataframes y boxplots
#subdfs <- split(data, as.factor(as.vector(unlist(data[divider])))) #con base a... hacer la división

Testing()