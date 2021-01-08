setwd('C:/Users/shyla/Desktop/Studium/TH/2Sem/DIS08/assignement2/dis08-assignment-2-thegreenhorns')
genres=read.csv("Exercise02.Bonus.FilmgenresSwitched.csv")

library(ggplot2)
library(RColorBrewer)


library(tidyverse)
getPalette = colorRampPalette(brewer.pal(9, "Paired"))

# group Data
genres %>% 
  mutate(Year = as.Date(paste0(Year, "-01-01"))) %>%
  gather(Genres, value, Comedy:OhneGenre) %>%
  
# plot
  ggplot(aes(x=Year, y=value, fill=Genres))+ 
  geom_area(position ="fill",alpha=0.8 , size=0.5, colour="white")+
  
# legend
  scale_fill_manual(values = getPalette(27))+
  scale_y_continuous( expand = c(0,0), labels = scales::percent)+
  scale_x_date(expand = c(0,0))+
  theme_bw() + 
  theme(panel.border = element_blank(), panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))+
  theme(plot.title = element_text(hjust = 0.5, size=18))+
labs(x = "Year", y = "Movies per Year", title = "Figure 3. Percentage distribution of movie genres over time")


    
