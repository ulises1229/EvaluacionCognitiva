text <- c("Because I could not stop for Death -",
          "He kindly stopped for me -",
          "The Carriage held but just Ourselves -",
          "and Immortality")
text

install.packages ("dplyr")

library(dplyr)

text_df <- data_frame(line = 1:4, text = text)

text_df

install.packages("tidytext")

library("tidytext")

text_df %>%
  unnest_tokens(word, text)

#Argumento to_lower para evitar que se quiten las mayusculas

text_df %>%
  unnest_tokens(word, text, to_lower = FALSE)

library(janeaustenr)
library(dplyr)
library(stringr)


original_books <- austen_books() %>%
  group_by(book) %>%
  mutate(linenumber = row_number(),
         chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]",
                                                 ignore_case = TRUE)))) %>%
  ungroup()

original_books


library(tidytext)
tidy_books <- original_books %>%
  unnest_tokens(word, text)

tidy_books

#Funcion anti_join para quitar stop words (palabras irrelevantes)
data(stop_words)
tidy_books <- tidy_books %>%
  anti_join(stop_words)

tidy_books

tidy_books %>%
  count(word, sort = TRUE) 

#desde aqui estuve moviendo en pinker

library(ggplot2)

tidy_books %>%
  count(word, sort = TRUE) %>%
  filter(n > 600) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

#Con el paquete gutenberg vamos a poder acceder a una gran cantidad de textos literarios de dominio
#publico.

install.packages("gutenbergr")
library(gutenbergr)

#En estos ejemplos vamos  descartar obras clasicas de distintos autores (hgwells, hermanas bronte) para
#comparar frecuencias de palabras y graficar

#Obras de H.G Wells

hgwells <- gutenberg_download(c(35, 36, 5230, 159))
tidy_hgwells <- hgwells %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

tidy_hgwells 

tidy_hgwells %>%
  count(word, sort = TRUE)

#Obras de las hermanas Bronte

bronte <- gutenberg_download(c(1260, 768, 969, 9182, 767))

tidy_bronte <- bronte %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

tidy_bronte

tidy_bronte %>%
  count(word, sort = TRUE)

library(tidyr)

frequency <- bind_rows(mutate(tidy_bronte, author = "Brontë Sisters"),
                       mutate(tidy_hgwells, author = "H.G. Wells"), 
                       mutate(tidy_books, author = "Jane Austen")) %>% 
  mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `Brontë Sisters`:`H.G. Wells`)

frequency

library(scales)

# expect a warning about rows with missing values being removed
# esperar una advertencia acerca de las filas con valores perdidos que se eliminan

ggplot(frequency, aes(x = proportion, y = `Jane Austen`, color = abs(`Jane Austen` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "Jane Austen", x = NULL)


