from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *

#Get set of marked rows in data table
dataTable = Document.Data.Tables["DCA Parameters"]
rowIndexSet=Document.ActiveMarkingSelectionReference.GetSelection(dataTable).AsIndexSet()


#check that only 1 row is marked
if rowIndexSet.Count == 1:
	col1 = dataTable.Columns["API"].RowValues.GetFormattedValue(rowIndexSet.First)
	col2 = dataTable.Columns["PROPNUM"].RowValues.GetFormattedValue(rowIndexSet.First)
	#dummy = dataTable.Columns["IP"].RowValues.GetFormattedValue(rowIndexSet.First)
	#get current columns in data table, including dummy column  
	#col2 = dataTable.Columns["Column 2"].RowValues.GetFormattedValue(rowIndexSet.First)
	#col1 = dataTable.Columns["Column 1"].RowValues.GetFormattedValue(rowIndexSet.First)
	#dummy = dataTable.Columns["Dummy Column"].RowValues.GetFormattedValue(rowIndexSet.First)

	 
	#delete marked row
	selectedRows = Document.ActiveMarkingSelectionReference.GetSelection(dataTable)
	dataTable.RemoveRows(selectedRows)

	#Create replacement row using existing data plus our document property OilIP
	#\r\n used for newline
	#OilIP is a document property
	NPVTen = NPVTen/1000000
	IRR = float(IRR)/100
	data_for_new_row= str(col1)+ ","+ str(col2) + "," + str(OilIP)  + "," + str(OilB)  + "," + str(OilDi)  + "," + str(OilDmin)  + "," + str(DaysFlat) + "," + str(OilTechnicalEUROne) + "," + str(GasIP) + "," + str(GasB)+ "," + str(GasDi)+ "," + str(GasDmin)+ "," + str(GasDaysFlat)+ "," + str(GasTechnicalEUROne)+ "," + str(CumOilatDaysFlat)+ "," + str(Cum) + "," + str(MonthsProduced) + "," + str(CommercialEUR) + "," + str(NPVTen)+ "," + str(IRR) 
	textData = "API,PROPNUM,Oil IP,Oil B,Oil Di,Oil Dmin,Oil Days Flat,Oil Technical EUR,Gas IP,Gas B,Gas Di,Gas Dmin,Gas Days Flat,Gas Technical EUR,Cum Oil at Days Flat,Cum,Months Produced,Commercial EUR,NPV-10,IRR\r\n" + data_for_new_row + "\r\n"

	#Memory Stream stuff
	stream = MemoryStream()
	writer = StreamWriter(stream)
	writer.Write(textData)
	writer.Flush()
	stream.Seek(0, SeekOrigin.Begin)

	#Define settings for data import and add new row
	readerSettings = TextDataReaderSettings()
	readerSettings.Separator = ","
	readerSettings.AddColumnNameRow(0)
	readerSettings.SetDataType(0, DataType.Real)
	readerSettings.SetDataType(1, DataType.String)
	readerSettings.SetDataType(2, DataType.Real)
	readerSettings.SetDataType(3, DataType.Real)
	readerSettings.SetDataType(4, DataType.Real)
	readerSettings.SetDataType(5, DataType.Real)
	readerSettings.SetDataType(6, DataType.Real)
	readerSettings.SetDataType(7, DataType.Real)
	readerSettings.SetDataType(8, DataType.Real)
	readerSettings.SetDataType(9, DataType.Real)
	readerSettings.SetDataType(11, DataType.Real)
	readerSettings.SetDataType(12, DataType.Real)
	readerSettings.SetDataType(13, DataType.Real)
	readerSettings.SetDataType(14, DataType.Real)
	readerSettings.SetDataType(15, DataType.Real)
	readerSettings.SetDataType(16, DataType.Real)
	readerSettings.SetDataType(17, DataType.Real)
	readerSettings.SetDataType(18, DataType.Real)
	readerSettings.SetDataType(19, DataType.Real)
	readerSettings.SetDataType(20, DataType.Real)






	textDataSource = TextFileDataSource(stream,readerSettings)
	settings = AddRowsSettings(dataTable,textDataSource)
	dataTable.AddRows(textDataSource,settings)