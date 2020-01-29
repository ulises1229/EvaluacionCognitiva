getwd()
setwd("/media/pinker/KINGSTON/tidytext_2/graficas_comparativas/")
getwd()

lineas3 <- read.csv("/media/pinker/KINGSTON/tidytext_2/frec_respuestas_por_item/secundaria/lineas3.csv")
lineas4 <- read.csv("/media/pinker/KINGSTON/tidytext_2/frec_respuestas_por_item/primaria/lineas3.csv")

#install.packages ("dplyr")
#install.packages("tidytext")
#install.packages("tidyr")

#library(dplyr)
#library(tidytext)
#library(tidyr)

frequency_lines34 <- bind_rows(mutate(lineas3, author = "secundaria"),
                               mutate(lineas4, author = "primaria")) %>% 
  #mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `primaria`)

frequency_lines34

View(frequency_lines34)

write.csv(frequency_lines34,"frecuencias_a3_ps.csv")

#install.packages("scales")
#install.packages("ggplot2")

library(scales)
library(ggplot2)

pdf("10_frecuentes_a1_ps_reord.pdf")

ggplot(frequency_lines34, aes(x = proportion, y = `secundaria`, color = abs(`secundaria` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "secundaria", x = NULL)

dev.off()

