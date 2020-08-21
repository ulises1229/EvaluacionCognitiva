#Script para sacar frecuencia de oraciones de las bases de datos de metaforas completas. En este ejemplo,
#trabajaremos con las bases de datos de niños primaria (3.csv) y niñas primaria (4.csv)

getwd()
setwd("/media/pinker/KINGSTON/tidytext")
getwd()

data3 <- read.csv('3.csv', header = T)
data3
View(data3)

text3 <-data3$Reactivo.1
text3

mode(text3)
text_3<-as.character(text3)
mode(text_3)

library(dplyr)

text_df_3 <- data_frame(line = 1:216, text = text_3)
text_df_3
View(text_df_3)

library("tidytext")

#token="lines"= Funciona similar a "sentences", pero aqui, la tokenizacion se basa en renglones 
#(sin importar si dentro del mismo renglon hay distintas oraciones, es decir, separaciones por 
#puntos y mayusculas, como en "sentences")

lineas3<- text_df_3 %>%
  unnest_tokens(word,text, token="lines")

lineas3
View(lineas3)

#Conteo de frecuencias
#Vamos a tokenizar por lines, ya que lo que queremos, son las
#respuestas completas de cada participante por cada item, y no dividiralas por oraciones

library(dplyr)
library(stringr)

conteo3 <- lineas3 %>%
  count(word, sort = TRUE)

View(conteo3)

write.csv(conteo3,"frecuencia_h_a1.csv")

library(ggplot2)

lineas3 %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()


#Ahora, vamos a repetir el mismo procedimiento, pero con el archivo de las niñas (4.csv)

data4 <- read.csv('4.csv', header = T)
data4
View(data4)

text4 <-data4$Reactivo.1
text4

mode(text4)
text_4<-as.character(text4)
mode(text_4)

library(dplyr)
text_df_4 <- data_frame(line = 1:212, text = text_4)
text_df_4

library("tidytext")

lineas4<- text_df_4 %>%
  unnest_tokens(word,text, token="lines")

lineas4
View(lineas4)

library(dplyr)
library(stringr)

conteo4 <- lineas4 %>%
  count(word, sort = TRUE)

View(conteo4)

write.csv(conteo4,"frecuencia_m_a1.csv")


library(ggplot2)

lineas4 %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()


#Esto de las frecuencias no sale, checar que es lo que esta pasando

library(tidyr)

frequency_lines34 <- bind_rows(mutate(lineas3, author = "ninos"),
                             mutate(lineas4, author = "ninas")) %>% 
  #mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `ninas`)

frequency_lines34

View(frequency_lines34)

write.csv(frequency_lines34,"frecuencias_a1_hm_prim.csv")


library(scales)

pdf("grafica1.pdf")

ggplot(frequency_lines34, aes(x = proportion, y = `ninos`, color = abs(`ninos` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "ninos", x = NULL)

dev.off()


jpeg("grafica1.jpeg")

ggplot(frequency_lines34, aes(x = proportion, y = `ninos`, color = abs(`ninos` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "ninos", x = NULL)

dev.off()

