

#clase
#variables
#setClass("Test", slots = list(type = "character", pvalue = ""))



definition <- function(p, tag){
  if(tag == "norm"){if(p<=0.05){return('otra d.')}else{return('d. normal')}}
  #if(tag == "vars"){if(p<=0.05){return('dierentes')}else{return('iguales')}} 
  #if(tag == "difs"){if(p<=0.05){return('otra d.')}else{return('d. normal')}}
}

names_changer <- function(){
  if(x == "norm"){
    names(df)[names(df) == "stat"] <- paste0(tests_names[z],"_stadistico")
    names(df)[names(df) == "pvalor"] <- paste0(tests_names[z], "_pvalor")
    names(df)[names(df) == "defins"] <- paste0(tests_names[z], "_distribucion")
  }
  else if(x == "vars"){
    names(df)[names(df) == "grados"] <- paste0(tests_names[z], "_grados_libertad")
    
  }
  else if(x == "difs_sex"){
    
  }

}

caller <- function(vec, val, tag){
  if(tag == "norm"){
    if(val == 1){jarque.test(vec)}
    else if(val == 2){ad.test(vec)}
    else if(val == 3){lillie.test(vec)}
    else if(val == 4){pearson.test(vec)}
    else if(val == 5){sf.test(vec)}
    else if(val == 6){shapiro.test(vec)}
  }
  else if(tag == "vars"){
    if(val == 1){bartlett.test(vec)}
    else if(val == 2){levene.test(vec)}
  }
  else if(tag == "difs"){
    if(val == 1){wilcox.test(vec)}
  }
  else if(tag == "difs_grup"){
    if(val == 1){kruskal.test(vec)}
  }
}

testing <- function(dataframe, tag){
  general_vars <- dataframe[,7:13] #variable que selecciona los datos deseados
  tests_names_norm <- c("jarque", "anderson", "kolmogorov", "pearson", "shapfran", "shapwilk") #esto cambia también
  #tests_names_vars <- c("bartlett", "levene")
  variables <- names(general_vars)
  df <- data.frame(variables)
  for(z in 1:length(tests_names_norm)){
    for(i in dataframe[,7:13]){
      print(typeof(i))
      #termina el recorrido y empieza el siguiente test, recorrido por tests solo en norm
      test = caller(i,z, tag)
      statistics <- c() #Aqui varían las variables, posible función
      pvalues <- c()
      defs <- c()
      free_degrees <- c()
      statistics[length(statistics) + 1] <- test$statistic
      pvalues[length(pvalues) + 1] <- test$p.value
      free_degrees[length(free_degrees) + 1] <- test$parameter
      defs[length(defs) + 1] <-definition(test$p.value, tag)
    }
    
    #eliminar esto:
    df$paste0(tests_names_norm[z],"_stadistico") <- statistics
    df$paste0(tests_names_norm[z], "_pvalor") <- pvalues
    df$paste0(tests_names_norm[z], "_distribucion") <- defs
    print(df)
    quit(save="default", status = 0, runLast = TRUE)
    #df$free_degrees <- free_degrees
    #names(df)[names(df) == "stat"] <- paste0(tests_names[z],"_stadistico")
    #names(df)[names(df) == "pvalor"] <- paste0(tests_names[z], "_pvalor")
    #names(df)[names(df) == "defins"] <- paste0(tests_names[z], "_distribucion")
    
    #print(df)
  }
}




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




