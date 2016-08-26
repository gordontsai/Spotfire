from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import AddColumnsSettings, JoinType, DataColumnSignature, DataType
from Spotfire.Dxp.Data.Import import DataTableDataSource

#Define table references
DCA_Parameters = Application.Document.Data.Tables["DCA Parameters"]
Daily_Header = Application.Document.Data.Tables["Oxy Eag Daily Header"]


ColumnA = DataColumnSignature(Daily_Header.Columns["PROPNUM"])
ColumnB = DataColumnSignature(DCA_Parameters.Columns["PROPNUM"])


###Getting COlumn names for DCA Parameters table and all of the document propertys we want to save
OilIP = DCA_Parameters.Columns["Oil IP"].Name
OilB = DCA_Parameters.Columns["Oil B"].Name
OilDi = DCA_Parameters.Columns["Oil Di"].Name
OilDmin = DCA_Parameters.Columns["Oil Dmin"].Name
DaysFlat = DCA_Parameters.Columns["Oil Days Flat"].Name
OilTechnicalEUROne = DCA_Parameters.Columns["Oil Technical EUR"].Name
GasIP = DCA_Parameters.Columns["Gas IP"].Name
GasB = DCA_Parameters.Columns["Gas B"].Name
GasDi = DCA_Parameters.Columns["Gas Di"].Name
GasDmin = DCA_Parameters.Columns["Gas Dmin"].Name
GasDaysFlat = DCA_Parameters.Columns["Gas Days Flat"].Name
GasTechnicalEUROne = DCA_Parameters.Columns["Gas Technical EUR"].Name
CumOilatDaysFlat = DCA_Parameters.Columns["Cum Oil at Days Flat"].Name
Cum = DCA_Parameters.Columns["Cum"].Name
MonthsProduced = DCA_Parameters.Columns["Months Produced"].Name
CommercialEUR = DCA_Parameters.Columns["Commercial EUR"].Name
NPV10 = DCA_Parameters.Columns["NPV-10"].Name
IRRProperty = DCA_Parameters.Columns["IRR"].Name



#Remove oil DCA parameter colums before we readd them
if Daily_Header.Columns.Contains("Oil IP"):
	if OilIP == Daily_Header.Columns["Oil IP"].Name:
		Daily_Header.Columns.Remove("Oil IP")

if Daily_Header.Columns.Contains("Oil B"):
	if OilB == Daily_Header.Columns["Oil B"].Name:
		Daily_Header.Columns.Remove("Oil B")

if Daily_Header.Columns.Contains("Oil Di"):
	if OilDi == Daily_Header.Columns["Oil Di"].Name:
		Daily_Header.Columns.Remove("Oil Di")

if Daily_Header.Columns.Contains("Oil Dmin"):
	if OilDmin == Daily_Header.Columns["Oil Dmin"].Name:
		Daily_Header.Columns.Remove("Oil Dmin")

if Daily_Header.Columns.Contains("Oil Days Flat"):
	if DaysFlat == Daily_Header.Columns["Oil Days Flat"].Name:
		Daily_Header.Columns.Remove("Oil Days Flat")

if Daily_Header.Columns.Contains("Oil Technical EUR"):
	if OilTechnicalEUROne == Daily_Header.Columns["Oil Technical EUR"].Name:
		Daily_Header.Columns.Remove("Oil Technical EUR")

	#####Remove Gas Columns
if Daily_Header.Columns.Contains("Gas IP"):
	if GasIP == Daily_Header.Columns["Gas IP"].Name:
		Daily_Header.Columns.Remove("Gas IP")

if Daily_Header.Columns.Contains("Gas B"):
	if GasB == Daily_Header.Columns["Gas B"].Name:
		Daily_Header.Columns.Remove("Gas B")

if Daily_Header.Columns.Contains("Gas Di"):
	if GasDi == Daily_Header.Columns["Gas Di"].Name:
		Daily_Header.Columns.Remove("Gas Di")

if Daily_Header.Columns.Contains("Gas Dmin"):
	if GasDmin == Daily_Header.Columns["Gas Dmin"].Name:
		Daily_Header.Columns.Remove("Gas Dmin")

if Daily_Header.Columns.Contains("Gas Days Flat"):
	if GasDaysFlat == Daily_Header.Columns["Gas Days Flat"].Name:
		Daily_Header.Columns.Remove("Gas Days Flat")

if Daily_Header.Columns.Contains("Gas Technical EUR"):
	if GasTechnicalEUROne == Daily_Header.Columns["Gas Technical EUR"].Name:
		Daily_Header.Columns.Remove("Gas Technical EUR")

	####Rmove other miscellaneous columns
if Daily_Header.Columns.Contains("Cum Oil at Days Flat"):	
	if CumOilatDaysFlat == Daily_Header.Columns["Cum Oil at Days Flat"].Name:
		Daily_Header.Columns.Remove("Cum Oil at Days Flat")

if Daily_Header.Columns.Contains("Cum"):
	if Cum == Daily_Header.Columns["Cum"].Name:
		Daily_Header.Columns.Remove("Cum")

if Daily_Header.Columns.Contains("Months Produced"):
	if MonthsProduced == Daily_Header.Columns["Months Produced"].Name:
		Daily_Header.Columns.Remove("Months Produced")

if Daily_Header.Columns.Contains("Commercial EUR"):
	if CommercialEUR == Daily_Header.Columns["Commercial EUR"].Name:
		Daily_Header.Columns.Remove("Commercial EUR")

if Daily_Header.Columns.Contains("NPV-10"):
	if NPV10 == Daily_Header.Columns["NPV-10"].Name:
		Daily_Header.Columns.Remove("NPV-10")

if Daily_Header.Columns.Contains("IRR"):
	if IRRProperty == Daily_Header.Columns["IRR"].Name:
		Daily_Header.Columns.Remove("IRR")



####Define conditions for joins later
joinConditionMap = {ColumnA : ColumnB}
ignoredCols = []

 



#Remove B Value Column
#if Column_IP == Application.Document.Data.Tables["Daily Header"].Columns["IP"].Name:
	#Document.Data.Tables["Daily Header"].Columns.Remove("IP")

settings = AddColumnsSettings( joinConditionMap, JoinType.LeftOuterJoin, ignoredCols)
ds = DataTableDataSource(DCA_Parameters)
Daily_Header.AddColumns(ds, settings)

##Remove if there is second column that we use to merge by
if Daily_Header.Columns.Contains("PROPNUM (2)"):
	Daily_Header.Columns.Remove("PROPNUM (2)")

#this code joins columns from BakkenWells to Normalized Monthly Data