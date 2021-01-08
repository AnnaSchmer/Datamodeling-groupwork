genres=read.csv("Exercise02.Bonus.FilmgenresSwitched.csv")

library(ggplot2)
library(RColorBrewer)


library(tidyverse)
getPalette = colorRampPalette(brewer.pal(9, "Set1"))

# group Data
genres %>% 
  mutate(Year = as.Date(paste0(Year, "-01-01"))) %>%
  gather(Genre, value, Comedy:OhneGenre) %>%
  
# plot
  ggplot(aes(x=Year, y=value, fill=Genre))+ 
  geom_bar(stat="identity",alpha=1.2 , size=0.1, colour="white")+
  
# legend
  scale_fill_manual(values = getPalette(27))+
  scale_y_continuous( expand = c(0,0))+
  scale_x_date(expand = c(0,0))+
  theme_bw() + 
  theme(panel.border = element_blank(), panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))+
  theme(plot.title = element_text(hjust = 0.5, size=18))+
  
labs(
  x = "Year",
  y = "Movies per Year",
  title = "Figure 4. Comparison of movies per genre over time")
