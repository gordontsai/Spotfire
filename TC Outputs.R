Daily_Production <- read.csv("Daily Production.csv")

Days_Flat <- 46




###### Cum Oil Calculations
Cum_Oil <- numeric(nrow(Daily_Production))

Cum_Oil[1] <- Daily_Production$Oil[1]

for(i in 2:nrow(Daily_Production))
{
  if(i == 1)
  {
    Cum_Oil[i] <- Daily_Production$Oil[i]
    break
  } 
  if(Daily_Production$Well.Name[i] == Daily_Production$Well.Name[i-1]) {
    Cum_Oil[i] <- Cum_Oil[i-1]+Daily_Production$Oil[i]
  } else {
    Cum_Oil[i] <- Daily_Production$Oil[i]
  }

}
Daily_Production$Cum.Oil <- Cum_Oil

##### Cum_Oil Days Flat
Cum_Oil_Days_Flat <- numeric(nrow(Daily_Production))




View(Daily_Production)


#Cum_Oil_At_Days_Flat <- mean(Daily_Production$Cum.Oil.at.Days.Flat)/1000
  