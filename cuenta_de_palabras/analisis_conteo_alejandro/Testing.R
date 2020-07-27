
nominee_normal <- function(df, stats, pvals, tests_names, z){
  df$stat <- stats
  df$pvalor <- pvals
  print(stats)
  names(df)[names(df) == "stat"] <- paste0(tests_names[z],"_stadistico")
  print(pvals)
  names(df)[names(df) == "pvalor"] <- paste0(tests_names[z], "_pvalor")
  return(df)
}

testing <- function(dataframe){
  tests_names_norm <- c("jarque", "anderson", "kolmogorov", "pearson", "shapfran", "shapwilk")
  tests_varianza <- c('bartlett', 'levene')
  general_vars <- dataframe[,7:13]
  variables <- names(general_vars)
  df <- data.frame(variables)

  for(z in 1:length(tests_varianza)){
    statistics <- c()
    pvalues <- c()
    for(i in dataframe[,7:13]){ 
          class(i) <- c('varianza')
          test <- calcular(i,z)
          statistics[length(statistics) + 1] <- test$statistic
          pvalues[length(pvalues) + 1] <- test$p.value
          #print(statistics)
          #print(pvalues)
    }
    #print(statistics)
    df$stat <- statistics
    df$pvalor <- pvalues
    names(df)[names(df) == "stat"] <- paste0(tests_names_norm[z],"_stadistico")
    print(pvalues)
    names(df)[names(df) == "pvalor"] <- paste0(tests_names_norm[z], "_pvalor")
    
  }
  View(df)
}

calcular <- function(x, val)  {
  UseMethod('calcular') 
}
calcular.normalidad <- function(x,val)  {
  vec <- as.vector(x)
  if(val == 1){
    jarque.test(vec)
  }
  else if(val == 2){
    ad.test(vec)
  }
  else if(val == 3){
    lillie.test(vec)
  }
  else if(val == 4){
    pearson.test(vec)
  }
  else if(val == 5){
    sf.test(vec)
  }
  else if(val == 6){
    shapiro.test(vec)
  }
}

calcular.varianza <- function(x, val){
  print('Entramos')
  
  vec <- as.vector(x)
  if(val == 1){
    bartlett.test(vec)
  }
  #else if(val == 2){
  #  levene.test(vec)
  #}
}

