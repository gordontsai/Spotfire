from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import AddColumnsSettings, JoinType, DataColumnSignature, DataType
from Spotfire.Dxp.Data.Import import DataTableDataSource

ColumnA = DataColumnSignature(Document.Data.Tables["Daily Header"].Columns["API-14"])
ColumnB = DataColumnSignature(Document.Data.Tables["DCA Parameters"].Columns["API-14"])
###Getting COlumn names for DCA Parameters table and all of the document propertys we want to save
Oil_IP = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil IP"].Name
Oil_B = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil B"].Name
Oil_Di = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil Di"].Name
Oil_Dmin = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil Dmin"].Name
Oil_DaysFlat = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil Days Flat"].Name
Oil_Technical_EUR = Application.Document.Data.Tables["DCA Parameters"].Columns["Oil Technical EUR"].Name
Gas_IP = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas IP"].Name
Gas_B = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas B"].Name
Gas_Di = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas Di"].Name
Gas_Dmin = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas Dmin"].Name
Gas_DaysFlat = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas Days Flat"].Name
Gas_Technical_EUR = Application.Document.Data.Tables["DCA Parameters"].Columns["Gas Technical EUR"].Name
Cum_Oil_at_DaysFlat = Application.Document.Data.Tables["DCA Parameters"].Columns["Cum Oil at Days Flat"].Name
Cum = Application.Document.Data.Tables["DCA Parameters"].Columns["Cum"].Name
Months_Produced = Application.Document.Data.Tables["DCA Parameters"].Columns["Months Produced"].Name
Commercial_EUR = Application.Document.Data.Tables["DCA Parameters"].Columns["Commerical EUR"].Name
NPV10 = Application.Document.Data.Tables["DCA Parameters"].Columns["NPV-10"].Name
IRR = Application.Document.Data.Tables["DCA Parameters"].Columns["IRR"].Name



####Define conditions for joins later
joinConditionMap = {ColumnA : ColumnB}
ignoredCols = []

#Remove oil DCA parameter colums before we readd them
if Oil_IP == Application.Document.Data.Tables["Daily Header"].Columns["Oil IP"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil IP")

if Oil_B == Application.Document.Data.Tables["Daily Header"].Columns["Oil B"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil B")

if Oil_Di == Application.Document.Data.Tables["Daily Header"].Columns["Oil Di"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil Di")

if Oil_Dmin == Application.Document.Data.Tables["Daily Header"].Columns["Oil Dmin"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil Dmin")

if Oil_DaysFlat == Application.Document.Data.Tables["Daily Header"].Columns["Oil Days Flat"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil Days Flat")

if Oil_Technical_EUR == Application.Document.Data.Tables["Daily Header"].Columns["Oil Technical EUR"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Oil Technical EUR")

#####Remove Gas Columns
if Gas_IP == Application.Document.Data.Tables["Daily Header"].Columns["Gas IP"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas IP")

if Gas_B == Application.Document.Data.Tables["Daily Header"].Columns["Gas B"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas B")

if Gas_Di == Application.Document.Data.Tables["Daily Header"].Columns["Gas Di"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas Di")

if Gas_Dmin == Application.Document.Data.Tables["Daily Header"].Columns["Gas Dmin"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas Dmin")

if Gas_DaysFlat == Application.Document.Data.Tables["Daily Header"].Columns["Gas Days Flat"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas Days Flat")

if Gas_Technical_EUR == Application.Document.Data.Tables["Daily Header"].Columns["Gas Technical EUR"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Gas Technical EUR")

####Rmove other miscellaneous columns
if Cum_Oil_at_DaysFlat == Application.Document.Data.Tables["Daily Header"].Columns["Cum Oil at Days Flat"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Cum Oil at Days Flat")

if Cum == Application.Document.Data.Tables["Daily Header"].Columns["Cum"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Cum")

if Months_Produced == Application.Document.Data.Tables["Daily Header"].Columns["Months Produced"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Months Produced")

if Commercial_EUR == Application.Document.Data.Tables["Daily Header"].Columns["Commercial EUR"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("Commercial EUR")

if NPV10 == Application.Document.Data.Tables["Daily Header"].Columns["NPV-10"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("NPV-10")

if IRR == Application.Document.Data.Tables["Daily Header"].Columns["IRR"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("IRR")

#Remove B Value Column
#if Column_IP == Application.Document.Data.Tables["Daily Header"].Columns["IP"].Name:
	#Document.Data.Tables["Daily Header"].Columns.Remove("IP")

settings = AddColumnsSettings( joinConditionMap, JoinType.LeftOuterJoin, ignoredCols)
ds = DataTableDataSource(Document.Data.Tables["DCA Parameters"])
Document.Data.Tables["Daily Header"].AddColumns(ds, settings)
Document.Data.Tables["Daily Header"].Columns.Remove("Well Name (Header) (2)")

#this code joins columns from BakkenWells to Normalized Monthly Data