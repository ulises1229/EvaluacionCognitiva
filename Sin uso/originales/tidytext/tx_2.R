getwd()
#setwd("/misc/jasper/navarreten/metas_1")
#setwd("/media/navarreten/KINGSTON/metas1/split_halves")
#setwd("E:/metas_4")
getwd()

data <- read.csv('1.csv', header = T)
data
View(data)
text <-c("gato","perro","chango","mono","pato", "gato", "leon", "cisne", "chango","perro")

text <-data$Reactivo.1
text

mode(text)
text1<-as.character(text)
mode(text1)


library(dplyr)
text_df <- data_frame(line = 1:10, text = text1)
text_df

library("tidytext")

text_df %>%
  unnest_tokens(word,text)

#Argumento to_lower para evitar que se quiten las mayusculas

text_df %>%
  unnest_tokens(word, text, to_lower = FALSE)

library(dplyr)
library(stringr)

#Vamos a usar la variable tidy_books, como viene en el manual de tidytext, para ir lo mas apegado al
#manual, aunque en este ejercicio no tiene sentido llamarle tidy_books

tidy_books <- text_df %>%
  unnest_tokens(word,text)

tidy_books

#Entonces, esta instrucción será para obtener la frecuencia de aparición de cada palabra, del data.frame
#asignado a la variable que nombramos tidy_books

tidy_books %>%
  count(word, sort = TRUE) 

#Vamos a hacer lo mismo que hicimos con la lista de datos 1. Para ver que todo este bien y 
#poderlas comparar

data2 <- read.csv('2.csv', header = T)
data2
View(data2)

text2 <-data2$Reactivo.1
text2

text2<-as.character(text2)
text2

library(dplyr)
text_df2 <- data_frame(line = 1:10, text = text2)
text_df2

library("tidytext")

text_df2 %>%
  unnest_tokens(word,text)

text_df2 %>%
  unnest_tokens(word, text, to_lower = FALSE)

library(dplyr)
library(stringr)

tidy_books2 <- text_df2 %>%
  unnest_tokens(word,text)

tidy_books2

tidy_books2 %>%
  count(word, sort = TRUE) 

#Ahora vamos a graficar la frecuencia de palabras de cada data.frame (tidy_books y tidy_books2)

library(ggplot2)

tidy_books %>%
  count(word, sort = TRUE) %>%
  #filter(n > 600) %>% #Aqui comentarice esto xq señala filtro de +de 600 veces (no sirve para
  #este ejercicio, donde la frecuencia de palabras son 1 y 2. Quitando esto, todo salio bien)
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

tidy_books2 %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

#Ahora, vamos a hacer la comparacion. Primero empezare con solo 2 listas: data y data2 (1.csv y 2.csv)

#Nos vamos a saltar todo lo de gutemberg, porque aqui no vamos a utilizar ese material, sino nuestro
#propio material

#Error: Aqui traté de crear una variable mas, para (tidybooks3) para crear un objeto mas, pero no funciono
#tidy_books3 <- text_df %>%
  #unnest_tokens(word,text)
#tidy_books3
#tidy_books3 %>%
  #count(word, sort = TRUE) 

#Entonces aca lo que vamos a hacer es sacar un data.frame comparando la proporcion en que
#aparacen las diferentes palabras, en niños y en niñas

library(tidyr)

frequency <- bind_rows(mutate(tidy_books, author = "niños"),
                       mutate(tidy_books2, author = "niñas")) %>% 
  mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `niñas`)

frequency

View(frequency)

#Y ya con el marco de datos de frecuencias, ahora vamos a hacer una grafica donde
#se vea esta comparación

library(scales)

# expect a warning about rows with missing values being removed
# esperar una advertencia acerca de las filas con valores perdidos que se eliminan

ggplot(frequency, aes(x = proportion, y = `niños`, color = abs(`niños` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "niños", x = NULL)

#Estoy haciendo un experimento para tokenizar pero no por palabra
#sino por oracion

data <- read.csv('1.csv', header = T)
data
View(data)

text_oracion <-data$Reactivo.3
text_oracion

mode(text)
text_oracion_1<-as.character(text_oracion)
mode(text_oracion_1)

library(dplyr)
text_df_oracion_1 <- data_frame(line = 1:10, text = text_oracion_1)
text_df_oracion_1

library("tidytext")

#Asi es como se tokeniza por oraciones
#token="sentences"
#En el caso de sentences, la separacion se hace tomando como referencia donde hay punto y empieza
#con mayuscula (si no empieza con mayuscula, no hace la separacion)

oraciones<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="sentences")

oraciones
View(oraciones)

#Ahora vamos a ver que pasa con otras opciones de tokenizar
#token="characters"=Devuelve por caracteres

caracteres<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="characters")

caracteres
View(caracteres)

#token="character_shingles"=devueve tokens de conjunto de 3 letras
#ej. perro, lo divide asi per, err, rro (ignora espacios en blanco)

character_shingles<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="character_shingles")

character_shingles
View(character_shingles)

#token="ngrams"=Devuelve por conjuntos de 3 palabras (similar a character_shingles
#pero en vez de caracteres, palabras)
#P. ej: Devuelve por conjuntos de 3 palabras, Lo divide así: 
#Devuelve por conjuntos, por conjuntos de, conjuntos de 3, de 3 palabras

engramas<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="ngrams")

engramas
View(engramas)

#token="skip_ngrams"=Devuelve algo raro, es como parte la oracion en
#conjuntos de 1,2 y 3 palabras, y va haciendo diferentes combinatorias
#no entiendo ahora para que se pueda utilizar esto, pero en fin

skip_ngrams<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="skip_ngrams")

skip_ngrams
View(skip_ngrams)

#token="lines"= Funciona similar a "sentences", pero aqui, la tokenizacion se basa en renglones 
#(sin importar si dentro del mismo renglon hay distintas oraciones, es decir, separaciones por 
#puntos y mayusculas, como en "sentences")

lineas<- text_df_oracion_1 %>%
  unnest_tokens(word,text, token="lines")

lineas
View(lineas)

#Hay otras formas de tokenizar, pero esas ya no las probe, probarlas despues

#Ahora ya. Vamos a continuar

library(dplyr)
library(stringr)

oraciones %>%
  count(word, sort = TRUE) 

#Tal vez sea mejor en este caso tokenizar por lines, ya que lo que queremos, son las
#respuestas completas de cada participante por cada item, y no dividiralas por oraciones


lineas %>%
  count(word, sort = TRUE)

library(ggplot2)

lineas %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

#Ahora, vamos a repetir el mismo procedimiento, pero con el archivo de las niñas (2.csv)

data2 <- read.csv('2.csv', header = T)
data2
View(data2)

text_oracion2 <-data2$Reactivo.3
text_oracion2

mode(text_oracion2)
text_oracion_2<-as.character(text_oracion2)
mode(text_oracion_2)

library(dplyr)
text_df_oracion_2 <- data_frame(line = 1:10, text = text_oracion_2)
text_df_oracion_2

lineas2<- text_df_oracion_2 %>%
  unnest_tokens(word,text, token="lines")

lineas2
View(lineas2)

lineas2 %>%
  count(word, sort = TRUE)

lineas2 %>%
  count(word, sort = TRUE) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

#Esto de las frecuencias no sale, checar que es lo que esta pasando

library(tidyr)

frequency_lines <- bind_rows(mutate(lineas, author = "niños"),
                       mutate(lineas2, author = "niñas")) %>% 
  #mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `niñas`)

frequency_lines

View(frequency_lines)

library(scales)

ggplot(frequency_lines, aes(x = proportion, y = `niños`, color = abs(`niños` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "niños", x = NULL)
