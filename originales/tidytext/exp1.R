getwd()
setwd("/media/pinker/KINGSTON/tidytext")
getwd()

#data <- read.csv('5.csv', header = T)
#data
#View(data)

lineas3 <- read.csv('frec_respuestas_por_item/hombres/lineas7.csv')
lineas4 <- read.csv('frec_respuestas_por_item/mujeres/lineas7.csv')

#install.packages ("dplyr")
#install.packages("tidytext")
#install.packages("tidyr")

library(dplyr)
library(tidytext)
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

write.csv(frequency_lines34,"frecuencias_a7_hm_prim.csv")


#install.packages("scales")
#install.packages("ggplot2")

library(scales)
library(ggplot2)

pdf("frecuencias_a7_hm_prim.pdf")

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

#Esto creo que esta todo mal (intento falllido, de preferencia quitar)
lineas3
View(lineas3)
mode(lineas3)
lineas3.1<-as.character(lineas3)
View(lineas3.1)
mode(lineas3.1)


lineas4<-data$Reactivo.2
lineas4
View(lineas4)
mode(lineas4)
lineas4.1<-as.character(lineas4)
View(lineas4.1)
mode(lineas4.1)