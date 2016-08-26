library(ggplot2)
library(gstat)
library(sp)
library(maptools)

BakkenDataSet <- read.csv("~/R/BakkenDataSet.csv",header = TRUE)
df <- BakkenDataSet
df$x <- df$Long
df$y <- df$Lat

coordinates(df) = ~x + y
      
plot(df)

Long.min <- min(df$Long)
Long.max <- max(df$Long)
Lat.min <- min(df$Lat)
Lat.max <- max(df$Lat)


x.range <-as.numeric(c(Long.min, Long.max))
y.range <- as.numeric(c(Lat.min, Lat.max))

grd <- expand.grid(x = seq(from = x.range[1], to = x.range[2], by = 0.1), y = seq(from = y.range[1], 
                                              to = y.range[2], by = 0.1))

coordinates(grd) <- ~x + y
gridded(grd) <- TRUE 

plot(grd, cex = 1.5, col = "grey")
points(df, pch =1 , col = "red", cex = 1)