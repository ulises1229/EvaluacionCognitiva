#Función rm para borrar las variables que se encuentren en ese momento
rm(list = ls())

#Importación de librerías
library(ggplot2)
library(dplyr)
library(tidyr)
library(moments)
library(nortest)
library(lawstat)
library(ggthemes)

#Selección de espacio de trabajo
#IMPORTANTE: Colocar con doble diagonal inversa o con una diagonal normal la 
#división entre carpetas para que pueda ser leído por el equipo.
setwd('C:\\Users\\Alex Isasi\\Documents\\analisis_conteo_palabras\\analisis_conteo_alejandro')
data = read.csv('resultados_gens.csv', na.strings = c("", "NA")) #Muestras
first_link <- paste0(getwd(),'/tests_gensim') #Link donde se alojarán los resultados
variables <- names(data[17:31])
ids_vector <- names(data[1:16])
y <- 1
#Creación de primer directorio si no existe, si existe se omite este bloque.
if(!dir.exists(first_link)){
    dir.create(first_link)
}


#Función principal, hace:
#Corre el proceso de creación del data frame con las variables que se utilizarán.
#Separa la ejecución por tipo de test.
#Acomoda los datos resultantes para un mejor entendimiento.
testing <- function(data, type) {

   # quit(save="default", status = 0, runLast = TRUE)
    if(!dir.exists(type)){
        dir.create(type)
    }
    setwd(type)
    result <- data.frame(variables)
    test_names <- test_type(type)

        for(test in test_names){
            
            cont <- 0
            estadisticos <- c()
            pvalores <- c()
            conclusiones <- c()
            grados <- c()
            
            for(x in 17:31){    
                #quit(save="default", status = 0, runLast = TRUE)
                cont <- cont + 1
                var<-as.vector(unlist(data[,x]))
                grupo <- as.vector(unlist(data[,cont]))
                var <- var[!is.na(var)]
                grupo <- grupo[!is.na(grupo)]
                obj <- Test(test_type = test, vec_data = var, type = type, grupo = grupo)
                st <- executioner(obj)
                def_str <- get_conclusion(st$p.value)

                if(test == 'bartlett'){
                    grados[length(grados)+1] <- st$parameter
                }
                estadisticos[length(estadisticos)+1] <- st$statistic
                pvalores[length(pvalores)+1] <- st$p.value
                conclusiones[length(conclusiones)+1] <- def_str
            }
            
            result$stad <- estadisticos
            result$pval <- pvalores
            result$par <- grados
            result$concs <- conclusiones
            names(result)[names(result) == 'stad'] <- paste0(test,'_estadistico')
            names(result)[names(result) == 'pval'] <- paste0(test,'_pvalor')
            names(result)[names(result) == 'par'] <- paste0(test,'_grados')
            names(result)[names(result) == 'concs'] <- paste0(test,'_conclusion')
            print(result)
        }
    write.csv(result, file = paste0(type,'_indicador_','.csv'))
}


#Clase Test
Test <- function(test_type, vec_data, type, grupo){
    value <- list(tipo_test = test_type, vector_info = vec_data, tipo = type, group = grupo)
    attr(value, "class") <- type
    print(value)
}

#Manejo de excepciones en pruebas, esta función retorna en cero las pruebas
#que no pueden realizarse por los datos presentados.
is_error <- function(ex){
    tryCatch(ex,
             error = function(e){
                    message("Error, valores retornados en cero:\n", e)
                    res <- list("p.value" = 0, "statistic" = 0, "parameter" = 0)
                    return(res)
             })
}

#Función genérica para la ejecución de tests dependiendo del tipo
#que se esté corriendo en ese momento
executioner <- function(obj) {
    UseMethod("executioner")
}

#Impresión en caso de que 
executioner.default <- function(obj) {
    cat("Esta es una funcion generica")
}

#Función
executioner.normalidad <- function(obj) {
    if(obj$tipo_test == 'jarque'){
        print('Entra jarque')
        jarque.test(obj$vector_info)
    }
    else if (obj$tipo_test == 'anderson') {
        print('Entra Anderson')
        res <- is_error({ad.test(obj$vector_info)})
        return(res)
    }
    else if (obj$tipo_test == 'kolmogorov') {
       lillie.test(obj$vector_info)
    }
    else if (obj$tipo_test == 'pearson') {
       pearson.test(obj$vector_info)
    }
    else if (obj$tipo_test == 'shapfran') {
       sf.test(obj$vector_info)
    }
    else if (obj$tipo_test == 'shapwilk') {
       shapiro.test(obj$vector_info)
    }
    
}


#Función de test de homogeneidad de varianzas
executioner.varianzas <- function(obj) {
    if(obj$tipo_test == 'bartlett'){
        result <- is_error({bartlett.test(obj$vector_info ~ obj$group)})
    }
    else if (obj$tipo_test == 'levene') {
        result <- is_error({levene.test(obj$vector_info, obj$group)}) 
    }
    return(result)
}


#Test de diferencias de varianzas
executioner.diferencias <- function(obj) {
    if(obj$tipo_test == 'wilcox'){
        wilcox.test(obj$vector_info, obj$group)
    }
    else if (obj$tipo_test == 'kruskal'){
        result <- is_error({kruskal.test(obj$vector_info, obj$group )})
    }
    else if (obj$tipo_test == 'friedman'){
        result <- is_error({friedman.test(obj$vector_info, obj$group)})
    }
}

#Impresión de conclusiones
get_conclusion <- function(p){
    if(p <= 0.05){
        return('Rechaza hipotesis nula')
    } else {
       return('No puede rechazar hipotesis nula')
    }
}

#Definición de test por hacer (de esto dependerá el procedimiento correspondiente)
test_type <- function(type) {
    if(type == 'normalidad'){
        test_names <- c('jarque','anderson', 'kolmogorov', 'pearson', 'shapfran', 'shapwilk') 
    } else if (type == 'varianzas') {
        test_names <- c('bartlett', 'levene') #levene
    } 
    else if (type == 'diferencias') {
       test_names <- c('kruskal') #wilcox, kruskal, friedman
    }
    return(test_names)
}

plotting <- function(data, evals, ids, y){
    while (y <= length(evals)) {
        #HISTOGRAMA
        ph <- ggplot(data, aes_string(evals[y], fill = ids[y], color = ids[y])) +
            geom_histogram(binwidth = 0.01) +
            ggtitle(paste0("Histograma de: ", evals[y])) +
            labs(x = 'Valores', y = 'Frecuencia de resultados') + theme_bw()
        ggsave(paste0("histograma_",evals[y],".jpeg")) 
        
        #BOXPLOT
        pb <- ggplot(data, aes_string(x=ids[y], y=evals[y], fill=ids[y])) + 
            geom_boxplot(alpha=0.3) +
            ggtitle(paste0("Boxplot de: ",evals[y]))+
            labs(x = "grupos", y = "Rango de resultados")+
            theme(legend.position="none")
        ggsave(paste0("boxplot_",evals[y],".jpeg")) 
        
        y = y + 1
    }
}

#Pruebas por realizar
tests <- c('normalidad', 'varianzas', 'diferencias') #diferencias

#Loop para:
#Establecer el área de trabajo en determinado directorio.
#Correr la función principal para la ejecución de las pruebas

#Nota: Este loop inicia todo el proceso.
for(test in tests){
    setwd(first_link)
    testing(data, test)
}

setwd(first_link)
getwd()

graphics_folder <- 'graficas'
#Ejecución de gráficas
if(!dir.exists(graphics_folder)){
    dir.create(graphics_folder)
}
setwd(graphics_folder)
plotting(data, variables, ids_vector, y)






