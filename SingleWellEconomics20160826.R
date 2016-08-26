#Will need to be commented out because these are input parameters
OilIP <- 810
OilB <- .65
OilDi <- 65 #Should be in percent
OilDmin <- 6 #Should be in percent
GasIP <- 953
GasB <- .70
GasDi <- 63 #Should be in percent
GasDmin <- 6 #Should be in percent
GasShrink <- 35.6 #These are in percent aka divided by 100 in formulas below
Royalty <- 17.473858007705 #These are in percent aka divided by 100 in formulas below
NGLYield <- 99.1 #bbl/mmcf
Y1PriceOil <-41.94
Y2PriceOil <-45.44
Y3PriceOil <-47.36
Y4PriceOil <-48.42
Y5PriceOil <-49.29
Y6PriceOil <- 50.02
Y1PriceGas <-2.09
Y2PriceGas <-2.65
Y3PriceGas <-2.74
Y4PriceGas <-2.78
Y5PriceGas <-2.87
Y6PriceGas <- 2.99
SpudtoProduction <- 3
NGLPercentWTI <- 20 #Should be in percent aka divide by 100
OilDiffPercent <- -5 #Should be in Percent aka divide by 100
OilDiffDollar <-0
NGLDiffPercent <- 0 #Should be in Percent aka divide by 100
NGLDiffDollar <- 0
GasDiffDollar <- 0
GasDiffPercent <-.4
SevTaxOil <- 4.6 #Should be in Percent aka divide by 100
SevTaxGas <- 7.5 #Should be in Percent aka divide by 100
SevTaxNGL <- 7.5 #Should be in Percent aka divide by 100
AdValoremTax <- 2.0 #Should be in Percent aka divide by 100
DC <- 5860000
OpexFixed1 <- 15250 #$
OpexFixed2 <- 15250 #$
OpexFixed3 <- 15250 #$
InitialPeriod <- 12 #Months
SecondPeriod <- 48 #Months
OpexOil <- 4.50 #$/bbl
OpexNGL <- 0
OpexGasPre <- 0
OpexGasPost <- 0
#IRR <- 15 #This should be in percent


#Make DC Input in Millions

DC <- DC*1000000


#Revenue Calculation

#Calculated Oil DCA Variables
OilAexp <- -log(1-OilDmin/100)/12
OilAi <- (1/OilB*((1-OilDi/100)^(-OilB)-1))/12
OilTexp <- -((1/(OilB*log(1-(OilDmin/100)))+1/(OilAi*12*OilB)))*12
OilNpexp <- OilIP*365/12/(OilAi*(1-OilB))*(1-1/((1+OilAi*floor(OilTexp)*OilB)^((1-OilB)/OilB)))
OilQexp <- OilIP/((1+OilAi*(ceiling(OilTexp)-1)*OilB)^(1/OilB))

#Calculated Gas DCA Variables
GasAexp <- -log(1-GasDmin/100)/12
GasAi <- (1/GasB*((1-GasDi/100)^(-GasB)-1))/12
GasTexp <- -((1/(GasB*log(1-(GasDmin/100)))+1/(GasAi*12*GasB)))*12
GasNpexp <- GasIP*365/12/(GasAi*(1-GasB))*(1-1/((1+GasAi*floor(GasTexp)*GasB)^((1-GasB)/GasB)))
GasQexp <- GasIP/((1+GasAi*(ceiling(GasTexp)-1)*GasB)^(1/GasB))

#Oil Production Variables
t <- 1 #Months
Q_Cum_Oil <- numeric(600)
Q_Month_Oil <- numeric(600)
Q_Cum_Gas <- numeric(600)
Q_Month_Gas <- numeric(600)

#Calculating and storing Cum Oil Production in Q_Cum_Oil
for (t in 1:600){
  if(t < OilTexp){
    Q_Cum_Oil[t] <- OilIP*365/12/(OilAi*(1-OilB))*(1-1/(1+OilAi*t*OilB)^((1-OilB)/OilB))
  } else {
    Q_Cum_Oil[t] <- (OilQexp*365/12)/OilAexp*(1-exp(-OilAexp*(t-floor(OilTexp))))+OilNpexp
  }
}

#Calculating and storing Month Oil Production in Q_Month_Oil
for(i in 1:600)
{
  if (i == 1 ){
    Q_Month_Oil[1] <- Q_Cum_Oil[1]
  } else {
    Q_Month_Oil[i] <- Q_Cum_Oil[i]-Q_Cum_Oil[i-1]
  }
}

#Gas Production Variables
t <- 1 #Months
Q_Cum_Gas <- numeric(600)
Q_Month_Gas <- numeric(600)

#Calculating and storing Cum Gas Production in Q_Cum_Gas
for (t in 1:600){
  if(t < GasTexp){
    Q_Cum_Gas[t] <- GasIP*365/12/(GasAi*(1-GasB))*(1-1/(1+GasAi*t*GasB)^((1-GasB)/GasB))
  } else {
    Q_Cum_Gas[t] <- (GasQexp*365/12)/GasAexp*(1-exp(-GasAexp*(t-floor(GasTexp))))+GasNpexp
  }
}

#Calculating and storing Month Gas Production in Q_Month_Gas
for(i in 1:600)
{
  if (i == 1 ){
    Q_Month_Gas[1] <- Q_Cum_Gas[1]
  } else {
    Q_Month_Gas[i] <- Q_Cum_Gas[i]-Q_Cum_Gas[i-1]
  }
}

#Net Production Calculations
Net_Gas <- numeric(600)
Net_NGL <- numeric(600)
Net_Oil <- numeric(600)
Net_Gas_Draft <- numeric(600)
Net_NGL_Draft <- numeric(600)
Net_Oil_Draft <- numeric(600)
Net_Gas_Draft <- Q_Month_Gas*(1-(GasShrink/100))*(1-(Royalty/100))
Net_NGL_Draft <- Q_Month_Gas*(NGLYield/1000)*(1-(Royalty/100))
Net_Oil_Draft <- Q_Month_Oil*(1-(Royalty/100))

#Move the array forward to take into account Spud to Production date
x <- 1

for(a in (SpudtoProduction):600){
  Net_Oil[SpudtoProduction+x] <- Net_Oil_Draft[x]
  Net_NGL[SpudtoProduction+x] <- Net_NGL_Draft[x]
  Net_Gas[SpudtoProduction+x] <- Net_Gas_Draft[x]
  x <- x + 1
}

#GetCurrentDate
CurrentDate <- Sys.Date()
dateMonth <- format(CurrentDate, format = "%m")
dateYear <- format(CurrentDate, format = "%Y")
intMonth <- as.integer(dateMonth)
intYear <- as.integer(dateYear)

#Create Price Deck Array
OilPD <-numeric(600)
NGLPD <-numeric(600)
GasPD <-numeric(600)
i <- 0
b <- 0

for (a in 1:(14-intMonth)){
  OilPD[a] <-Y1PriceOil
  NGLPD[a] <-Y1PriceOil*(NGLPercentWTI/100)
  GasPD[a] <-Y1PriceGas
}
while(i<12){
  OilPD[14-intMonth+i] <- Y2PriceOil
  NGLPD[14-intMonth+i] <- Y2PriceOil*(NGLPercentWTI/100)
  GasPD[14-intMonth+i] <- Y2PriceGas
  i <- i + 1
}
while(i<24){
  OilPD[14-intMonth+i] <- Y3PriceOil
  NGLPD[14-intMonth+i] <- Y3PriceOil*(NGLPercentWTI/100)
  GasPD[14-intMonth+i] <- Y3PriceGas
  i <- i + 1
}
while(i<36){
  OilPD[14-intMonth+i] <- Y4PriceOil
  NGLPD[14-intMonth+i] <- Y4PriceOil*(NGLPercentWTI/100)
  GasPD[14-intMonth+i] <- Y4PriceGas
  i <- i + 1
}
while(i<48){
  OilPD[14-intMonth+i] <- Y5PriceOil
  NGLPD[14-intMonth+i] <- Y5PriceOil*(NGLPercentWTI/100)
  GasPD[14-intMonth+i] <- Y5PriceGas
  i <- i + 1
}
for(a in (14-intMonth+48):600)
{
  OilPD[14-intMonth+48+b] <- Y6PriceOil
  NGLPD[14-intMonth+48+b] <- Y6PriceOil*(NGLPercentWTI/100)
  GasPD[14-intMonth+48+b] <- Y6PriceGas
  b <- b + 1
}

#BasisDifferential Arrays
OilDiff <- OilDiffDollar+((OilDiffPercent/100)*OilPD)
NGLDiff <- NGLDiffDollar+((NGLDiffPercent/100)*NGLPD)
GasDiff <- GasDiffDollar+((GasDiffPercent/100)*GasPD)

#Realized Price
OilRealized <- OilPD+OilDiff
NGLRealized <- NGLPD+NGLDiff
GasRealized <- GasPD+GasDiff #Do we care about Heat Rate?

#Revenue Calculation
RevenueOil <- numeric(600)
RevenueNGL <- numeric(600)
RevenueGas <- numeric(600)
Revenue <- numeric(600)
for(a in 1:600)
{
  RevenueOil[a] <- OilRealized[a]*Net_Oil[a]
  RevenueNGL[a] <- NGLRealized[a]*Net_NGL[a]
  RevenueGas[a] <- GasRealized[a]*Net_Gas[a]
}
Revenue <- RevenueOil+RevenueNGL+RevenueGas

#End of Revenue Calculation

#Cost Calculation

#Severance Tax Calculation
SevCostOil <- numeric(600)
SevCostNGL <- numeric(600)
SevCostGas <- numeric(600)
SevCost <- numeric(600)

SevCostOil <- RevenueOil*(SevTaxOil/100)
SevCostNGL <- RevenueNGL*(SevTaxNGL/100)
SevCostGas <- RevenueGas*(SevTaxGas/100)
SevCost <- SevCostOil + SevCostNGL + SevCostGas

#Ad Valorem Tax
AdVCost <- numeric(600)
AdVCost <- (Revenue - SevCost)*(AdValoremTax/100)

#D&C Cost
DCCost <- numeric(600)
DCCost[1] <- DC

#Opex

#Fixed Opex
OpexFixedCost <- numeric(600)
a <- 0
x <- 1

#Initial Opex
for(a in (SpudtoProduction):(SpudtoProduction+InitialPeriod-1)){
  OpexFixedCost[SpudtoProduction+x] <- OpexFixed1
  x <- x + 1
}

#Second Opex
x <- 1
for(a in (SpudtoProduction+InitialPeriod-1):(SpudtoProduction+InitialPeriod+SecondPeriod-1)){
  OpexFixedCost[SpudtoProduction+x+InitialPeriod] <- OpexFixed2
  x <- x + 1
}

#Remaining Opex
x <- 1
for(a in (SpudtoProduction+InitialPeriod+SecondPeriod-1):598){
  OpexFixedCost[SpudtoProduction+x+InitialPeriod+SecondPeriod] <- OpexFixed3
  x <- x + 1
}

#Commodity Opex
OpexOilCost <- numeric(600)
OpexNGLCost <- numeric(600)
OpexGasCost <- numeric(600)
x <- 1

for(a in (SpudtoProduction):599){
  
  OpexOilCost[SpudtoProduction+x] <- Q_Month_Oil[x]*OpexOil
  OpexNGLCost[SpudtoProduction+x] <- Net_NGL[x]*OpexNGL
  OpexGasCost[SpudtoProduction+x] <- (Q_Month_Gas[x]*OpexGasPre)+(Q_Month_Gas[x]*(1-(Royalty/100))*OpexGasPost)
  x <- x + 1
}

#Total Opex
OpexCost <- OpexFixedCost + OpexOilCost + OpexNGLCost + OpexGasCost

#End of Cost

#Cash Flow
#Net Cash Flow
NetCashFlow <- numeric(600)
NetCashFlow <- Revenue - OpexCost - DCCost - AdVCost - SevCost

#Breakeven Month
BreakEven <- 3
for(a in 1:600)
{
  if(NetCashFlow[a] > 0)
  {
    BreakEven = BreakEven + 1
  } else {
  }
}

for(a in (BreakEven+1):600)
{
  Revenue[a] <- 0
  OpexCost[a] <- 0
  AdVCost[a] <- 0
  SevCost[a] <- 0
}

#Reassigns NetCashFlow inputting zero
NetCashFlow <- numeric(600)
NetCashFlow <- Revenue - OpexCost - DCCost - AdVCost - SevCost

#Daily NPV Date Calculation
months <- c(1,2,3,4,5,6,7,8,9,10,11,12,31,28,31,30,31,30,31,31,30,31,30,31)
Days <- numeric(12)
#NumDays <- c(31,28,31,30,31,30,31,31,30,31,30,31)
NumDays <- matrix(months, nrow=2, ncol=12, byrow=TRUE)
NumMonthDays <- numeric(12)
NumMonthDays2 <- numeric(600)
x<- 1
for(a in intMonth:12){
  Days[x] <- NumDays[1,a]
  x <- x+1
}
x <- x - 1

y <- 0

for(b in x:11)
{
  Days[x+1] <- NumDays[1,1+y]
  y <- y+1
  x <- x+1
}

for(a in 1:12)
{
  NumMonthDays[a] <- NumDays[2,Days[a]]
}

NumMonthDays2[1] <- 0
NumMonthDays2[2] <- NumMonthDays[1]-1+NumMonthDays[2]
for (a in 3:12)
{
  NumMonthDays2[a] <- NumMonthDays[a]
}

x<- 1
y <- 0
for(a in (13:600))
{
  if(x == 13)
  {
    x <- 1
    NumMonthDays2[a] <- NumMonthDays[x]
    x<- x+1
  } else{
    NumMonthDays2[a] <- NumMonthDays[x]
    x<- x+1
  }
}
#for(a in 1:599)
#{
#NumMonthDays2[a] <- NumMonthDays2[a+1]
#}

#NPV Daily
PV <- numeric(600)
DaySum <- numeric(600)
a <- 1
#if (a==1)
#{
#  DaySum1 <- 0
#  PV[a] <- NetCashFlow[a]/(((1+((IRR/100)))^(DaySum1)))
#}
for(b in 2:600)
{
  DaySum[b] <- DaySum[b-1] + NumMonthDays2[b]
}

#for (a in 1:600)
#{

#PV[a] <- NetCashFlow[a]/(1+(IRR/100))^(DaySum[a]/365)
#}
#NPVZero <- (sum(PV))

#NPV10
PV10 <- numeric(600)
DaySum <- numeric(600)
a <- 1
if (a==1)
{
  DaySum1 <- 0
  PV10[a] <- NetCashFlow[a]/(((1+((10/100)))^(DaySum1)))
}
for(b in 2:600)
{
  DaySum[b] <- DaySum[b-1] + NumMonthDays2[b]
}

for (a in 1:600)
{
  
  PV10[a] <- NetCashFlow[a]/(1+(10/100))^(DaySum[a]/365)
}
NPVTen <- (sum(PV10))


#NPV10
PV15 <- numeric(600)
DaySum <- numeric(600)
a <- 1
if (a==1)
{
  DaySum1 <- 0
  PV15[a] <- NetCashFlow[a]/(((1+((15/100)))^(DaySum1)))
}
for(b in 2:600)
{
  DaySum[b] <- DaySum[b-1] + NumMonthDays2[b]
}

for (a in 1:600)
{
  
  PV15[a] <- NetCashFlow[a]/(1+(15/100))^(DaySum[a]/365)
}
NPVFifteen <- (sum(PV15))


pv.simple <- function(r,n,fv){
  return((fv/(1+r)^(n/365))*(-1))
}

pv.uneven <- function(r,t,cf){
  n <- length(cf)
  sum <- 0
  for(i in 1:n){
    sum <- sum + pv.simple(r,t[i],cf[i])
  }
  return(sum)
}

irr <- function(cf,time){
  n <- length(cf)
  subcf <- cf[2:n]
  subt <- time[2:n]
  uniroot(function(r) -1 * pv.uneven(r,subt,subcf) + cf[1], interval=c(1e-10,1e10))$root
}


if(sum(NetCashFlow) > 0 ){
  IRRValue <- irr(NetCashFlow,DaySum)*10000
  IRRValue <- as.integer(IRR)
} else {
  IRRValue <- 0
  IRRValue <- as.integer(IRR)
}