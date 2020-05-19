getwd()


ggplot(data, aes(x=as.factor(comparacion),y=(puntaje_similitud), fill=as.factor(comparacion))) + 
  geom_boxplot(alpha=0.5, notch = T) + 
  labs(title = "Diferencias entre Grupos")+
  ylab("Puntaje de Similitud")+
  xlab("Comparaciones")+
  scale_fill_brewer(palette="Set1") +
  theme_minimal()

ggsave("grafica_similitudes.jpeg")


ggplot(data1, aes(x=as.factor(comparacion),y=(puntaje_similitud), fill=as.factor(comparacion))) + 
  geom_boxplot(alpha=0.5, notch = T) + 
  labs(title = "Diferencias entre Grupos")+
  ylab("Puntaje de Similitud")+
  xlab("Comparaciones")+
  scale_fill_brewer(palette="Set1") +
  theme_minimal()

ggsave("grafica_similitudes_2.jpeg")