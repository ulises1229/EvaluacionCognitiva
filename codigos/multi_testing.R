#Multi Testing
#Este script calcula con base los datos que sean ingresados y lo que se desee las siguientes pruebas estadisticas:
#Para normalidad: Jarque test, Anderson test, kolmogorov, pearson, shapiro-francia, shapiro-wilk
#Para homogeneidad de varianzas: Bartlett test, Levene test
#Para diferencia de varianzas(dependiendo de los datos ingresados Wilcox test/U de Mann Whitney, kruskal wallis
#Borrado de variables existentes
#rm(list = ls())

#Instalaci贸n de librerias necesarias (en caso de no tenerlas)
#install.packages(c("ggplot2",
#                   "stats",
#                   "dplyr",
#                   "tidyr",
#                   "moments",
#                   "nortest",
#                   "lawstat",
#                   "ggthemes",
#                   "FSA"))

#Librerias
library(ggplot2)
library(stats)
library(dplyr)
library(tidyr)
library(moments)
library(nortest)
library(lawstat)
library(ggthemes)
library(FSA)

get_names <- function(type, numGroups) { #Funci贸n que retorna la columna con tipos de test deseados dependiendo del tipo que ingrese a la funci贸n
  vec_tot_of_names <- c()
  if(type == 'normalidad'){ test_names <- list('jarque','anderson', 'kolmogorov', 'pearson', 'shapfran', 'shapwilk')}
  if (type == 'homogeneidad') { test_names <- list('bartlett', 'levene')} #levene
  if (type == 'diferencias' & numGroups <= 2) { test_names <- list('Wilcox')}
  else if(type == 'diferencias' & numGroups > 2){ test_names <- list('Kruskal') }
  
  for(t in test_names){
    vec_of_names <- paste0(t, c('_estadistico', '_pvalor', '_conclusion'))
    vec_tot_of_names <- c(vec_tot_of_names, vec_of_names)
  }
  return(vec_tot_of_names)
}

#Funcion que hace graficas de caja (boxplots)
get_plot <- function(column, grp, df){
  print(as.vector(unlist(df[column])))
  rango <- max(as.vector(unlist(df[column])), na.rm = T)
  print(rango)
  themes = c("PuBu", "GnBu", "OrRd", "YlGn", "PuRd", "BuPu", "Dark2", "YlOrBr")
  
  p <- ggplot(df, aes_string(x=grp, y=column, group=grp, fill = as.factor(grp))) +
    geom_boxplot() +
    geom_jitter(shape=16, position = position_jitter(0.1)) +
    scale_y_continuous(breaks = seq(0, rango, 2)) + 
    scale_fill_brewer(palette = sample(themes,1)) +
    labs(x = grp, y = column, title=paste0("Comparaciones de ", column, " entre cada ", grp))
  ggsave(paste0("boxplot_", column, ".png"), width = 12)
}

#Funci贸n que organiza dataframes en directorios y los guarda como CSV's
organizer <- function(list_dataframes){
  x = 1
  for(df in list_dataframes){
    write.csv(df, file = paste0(names(list_dataframes[x]),'.csv')) #ejemplo: normalidad_todo, diferencias_ph_vs_pm.csv
    x = x + 1
  }
}

#Funci贸n que retorna la columna de resultados dependiendo de la columna analizada y el test ejecutado
get_column <- function(list_of_tests){
  column <- c()
  for(test in list_of_tests){
    new_data <- c(test$statistic, test$p.value, get_conclusion(test$p.value))
    column <- c(column, new_data)
  }
  return(column)
}


#Agregar a esta funci贸n el tiepo de test para que devuelva cadena dependiendo del tipo
get_conclusion <- function(pvalor){ 
  if(pvalor <= 0.05){
    return('Rechaza la hipotesis nula')
  } else{
    return('No rechaza la hipotesis nula')
  }
}


counterGroups <- function(data, grupo){
  x <- length(unique(as.vector(unlist(data[grupo]))))
  return(x)
}

#Funcion que regresa resultados de tests de homogeneidad de varianza
testing_homogeneity <- function(variable, group){
  column <- c()
  list_of_tests <- list(bartlett.test(variable~group), #bartlett
                        levene.test(variable, group)) #levene
  
  col <- get_column(list_of_tests)
  return(col)
}

testing_difference <- function(variable, group, numGroups){
  if(numGroups >= 3){
    test <- list(kruskal.test(variable, group))
  } else if(numGroups == 2){
    test <- list(wilcox.test(variable ~ group))
  }
  
  col <- get_column(test)
  return(col)
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

dunn <- function(variable, grp, dat){
  dunnT <- dunnTest(as.vector(unlist(dat[variable])), as.factor(as.vector(unlist(dat[grp]))))
  print(dunnT)
  dunnT_as_df <- as.matrix.data.frame(dunnT$res)
  write.csv(dunnT_as_df, file = paste0(variable, '_dunn.csv'))
}


procedure <- function(data, grupo ,colsToAnalyze, normalidad, homogeneidad_de_varianzas, diferencias_de_varianzas, numGroups){
  for(i in colsToAnalyze){
    variable <- as.vector(unlist(data[i]))
    group <- as.vector(unlist(data[grupo]))

    new_col_norm <- testing_normality(variable)
    normalidad <- cbind(normalidad, new_col_norm)

    new_col_homo <- testing_homogeneity(variable, group)
    homogeneidad_de_varianzas <- cbind(homogeneidad_de_varianzas, new_col_homo)
  
    new_col_diff <- testing_difference(variable, group, counterGroups(data, grupo))
    diferencias_de_varianzas <- cbind(diferencias_de_varianzas, new_col_diff)
    
    if(numGroups > 2){
      dunn(names(data[i]), names(data[grupo]), data)
    }
    
    get_plot(names(data[i]), names(data[grupo]), data)
    
  }
  
  x <- length(colsToAnalyze) + 1
  
  names(normalidad)[2:x] <- names(data)[colsToAnalyze]
  names(homogeneidad_de_varianzas)[2:x] <- names(data)[colsToAnalyze]
  names(diferencias_de_varianzas)[2:x] <- names(data)[colsToAnalyze]
  list_of_dataframes <- list(normalidad = normalidad,
                             homogeneidad_de_varianzas = homogeneidad_de_varianzas,
                             diferencias_de_varianzas = diferencias_de_varianzas) 
  
  organizer(list_of_dataframes)
}


main <- function(directorio, data, grupo){ #filtro, colsToAnalyze, nombreDest
  setwd(directorio)
  data <- read.csv(data, na.strings = c("", "NA"))
 
  first_link <- paste0(getwd(),'/',nombreDest)
  
  if(!dir.exists(first_link)){
    dir.create(first_link)
  }
  
  setwd(first_link)
  
  numGroups <- counterGroups(data, grupo)
  print(numGroups)
 
 normalidad <- data.frame(tests = get_names('normalidad', numGroups )) #dataframe de normalidad
 homogeneidad_de_varianzas <- data.frame(tests = get_names('homogeneidad', numGroups)) #dataframe de homogeneidad de varianzas
 diferencias_de_varianzas <- data.frame(tests = get_names('diferencias', numGroups)) #dataframe 1 de diferencia de varianzas
 
 procedure(data, grupo, colsToAnalyze, normalidad, homogeneidad_de_varianzas, diferencias_de_varianzas, numGroups)
 
 print(paste0('An醠isis finalizado, resultados en: ', getwd()))
}

main(directorio, data, grupo)
