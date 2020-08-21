analisis_item <- function (fileN, item){
  
data <- read.csv(fileN, header = T)
data

nombref <- paste("item_",item, ".csv", sep="")
nombref2 <- paste("lineas",item, ".csv", sep="")
nombref3 <- paste("item_",item, ".jpeg", sep="")

text <- data[,item]

text

mode(text)
texto<-as.character(text)
mode(texto)

library(dplyr)

text_lineas <- data_frame(line = 1:471, text = texto)
text_lineas

write.csv(text_lineas, nombref2, row.names = F)

library("tidytext")

lineas<- text_lineas %>%
  unnest_tokens(word,text, token="lines")

lineas
View(lineas)

write.csv(lineas, nombref2, row.names = F)

library(dplyr)
library(stringr)

conteo <- lineas %>%
  count(word, sort = TRUE)

View(conteo)

write.csv(conteo, nombref)

library(ggplot2)

lineas %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

ggsave(nombref3)

}

#row.names = F)
