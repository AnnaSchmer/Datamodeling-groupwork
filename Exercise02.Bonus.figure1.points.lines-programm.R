setwd('C:/Users/shyla/Desktop/Studium/TH/2Sem/DIS08/assignement2/dis08-assignment-2-thegreenhorns')
genres=read.csv("Exercise02.Bonus.FilmgenresSwitched.csv")

library(ggplot2)
library(RColorBrewer)

getPalette = colorRampPalette(brewer.pal(9, "Set1"))

ggplot(genres, aes(x=Year)) + 
  geom_line(aes(y = Comedy, colour = "Comedy")) + 
  geom_line(aes(y = Drama, colour = "Drama")) +
  geom_line(aes(y = Action, colour = "Action")) +
  geom_line(aes(y = Biography, colour = "Biography")) +
  geom_line(aes(y = Crime, colour = "Crime")) +
  geom_line(aes(y = Music, colour = "y = Music")) +
  geom_line(aes(y = Western, colour = "Western")) +
  geom_line(aes(y = Romance, colour = "Romance")) +
  geom_line(aes(y = Mystery, colour = "Mystery")) +
  geom_line(aes(y = Animation, colour = "Animation")) +
  geom_line(aes(y = Short, colour = "Short")) +
  geom_line(aes(y = Family, colour = "Family")) +
  geom_line(aes(y = Adventure, colour = "Adventure")) +
  geom_line(aes(y = GameShow, colour = "GameShow")) +
  geom_line(aes(y = War, colour = "War")) +
  geom_line(aes(y = History, colour = "History")) +
  geom_line(aes(y = Documentary, colour = "Documentary")) +
  geom_line(aes(y = FilmNoir, colour = "FilmNoir")) +
  geom_line(aes(y = Musical, colour = "Musical")) +
  geom_line(aes(y = Fantasy, colour = "Fantasy")) +
  geom_line(aes(y = Thriller, colour = "Thriller")) +
  geom_line(aes(y = TalkShow, colour = "TalkShow")) +
  geom_line(aes(y = SciFi, colour = "SciFi")) +
  geom_line(aes(y = Horror, colour = "Horror")) +
  geom_line(aes(y = RealityTV, colour = "RealityTV")) +
  geom_line(aes(y = Sport, colour = "Sport")) +
  geom_line(aes(y = OhneGenre, colour = "OhneGenre"))+
  scale_fill_manual(values = getPalette(27))+
  labs(
    x = "Year",
    y = "Movies per Genre",
    color = "Genres",
    title = "Figure 1. Number of movies per genre over time")+ 
  scale_x_continuous(expand = c(0,0))+scale_y_continuous(expand = c(0,0))+
  theme_bw() + 
  theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))+
  theme(plot.title = element_text(hjust = 0.5, size=18))





