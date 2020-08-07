testing <- function(data, type, r) {
    
    if(!dir.exists(type)){
        dir.create(type)
    }
    setwd(type)
    variables <- names(data[,7:13])
    result <- data.frame(variables)
    test_names <- test_type(type)
    grupo <- data$nivel
        for(test in test_names){
            estadisticos <- c()
            pvalores <- c()
            conclusiones <- c()
            grados <- c()
            
            for(x in 7:13){
                var<-as.numeric(na.exclude(as.vector(unlist(data[,x]))))
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

Test <- function(test_type, vec_data, type, grupo){
    value <- list(tipo_test = test_type, vector_info = vec_data, tipo = type, group = grupo)
    attr(value, "class") <- type
    print(value)
}

executioner <- function(obj) {
    UseMethod("executioner")
}

executioner.default <- function(obj) {
    cat("Esta es una funcion generica")
}

executioner.normalidad <- function(obj) {
    if(obj$tipo_test == 'jarque'){
        print('Entra jarque')
        jarque.test(obj$vector_info)
    }
    else if (obj$tipo_test == 'anderson') {
       ad.test(obj$vector_info)
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
    #regresar test y dependiendo del test ejecutar otra función desde aqui para 
}

executioner.varianzas <- function(obj) {
    if(obj$tipo_test == 'bartlett'){
       test <- bartlett.test(obj$vector_info ~ obj$group)
       
    }
    else if (obj$tipo_test == 'levene') {
       test <- levene.test(obj$vector_info, obj$group)
    }
    return(test)
}

executioner.diferencias <- function(obj) {
    if(obj$tipo_test == 'wilcox'){
        print('Entra a wilcox')
        wilcox.test(obj$vector_info ~ obj$group)
    }
}
    
get_conclusion <- function(p){
    if(p <= 0.05){
        return('Rechaza hipotesis nula')
    } else {
       return('No puede rechazar hipotesis nula')
    }
}

test_type <- function(type) {
    if(type == 'normalidad'){
        test_names <- c('jarque', 'anderson', 'kolmogorov', 'pearson', 'shapfran', 'shapwilk')
    } else if (type == 'varianzas') {
        test_names <- c('bartlett', 'levene')
    } else if (type == 'diferencias') {
       test_names <- c('wilcox')
    }
    return(test_names)
}











