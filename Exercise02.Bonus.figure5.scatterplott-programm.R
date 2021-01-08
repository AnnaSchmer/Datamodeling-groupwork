genres=read.csv("Exercise02.Bonus.FilmgenresSwitched.csv")

library(ggplot2)
library(RColorBrewer)


library(tidyverse)
getPalette = colorRampPalette(brewer.pal(9, "Set1"))


# group Data
genres %>% 
  mutate(Year = as.Date(paste0(Year, "-01-01"))) %>%
  gather(Genre, value, Comedy:OhneGenre) %>%
  
# Reihung
#  fac=factor(fac, levels=as.character(c(1, 10, 2, 20, 3, 30, 4, 40) ) )
  
# plot
  ggplot(aes(x=Year, y=value, color=Genre))+ 
  geom_point(alpha=0.5, size=1)+
  geom_smooth(method = "lm", se=FALSE, color="black", formula = y ~ x)+
  facet_wrap(~Genre, ncol=9, nrow=3)+
  scale_fill_manual(values = getPalette(27))+
  
  
# legend
scale_y_continuous( expand = c(0,0))+
scale_x_date(expand = c(0,0))+
theme(strip.background = element_rect(fill = alpha("white")))+
theme(axis.ticks = element_line(), legend.position = "none")+
theme(strip.text.x = element_text(size=12))+
theme(panel.border = element_blank(), panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))+
theme(plot.title = element_text(hjust = 0.5, size=18))+
  labs(
  x = "",
  y = "",
  title = "Figure 5. Comparison of film genres over time")
