datos <- read.csv("mas_frecuentes_2_a1_ps_reord.csv")

ggplot(datos, aes(x=as.factor(palabra), y=frecuencia, fill=nivel escolar))+
  labs(title = "Frecuencia de respuestas por nivel escolar")+
  xlab("respuesta")+
  ylab("Frecuencia en porcentaje") +
  theme(axis.title.x = element_text(face="bold",size=10),plot.title = element_text(size=rel(1.5)))+
  geom_bar(position="dodge")+
  scale_fill_brewer(palette ="Set1")+
  theme_linedraw()

ggsave("mas_frecuentes_2_a1_ps_reord.jpeg")
