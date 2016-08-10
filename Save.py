from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *

#Get set of marked rows in data table
dataTable = Document.Data.Tables["DCA Parameters"]
rowIndexSet=Document.ActiveMarkingSelectionReference.GetSelection(dataTable).AsIndexSet()
print rowIndexSet
print rowIndexSet.Count

#check that only 1 row is marked
if rowIndexSet.Count == 1:
	col1 = dataTable.Columns["API-14"].RowValues.GetFormattedValue(rowIndexSet.First)
	print col1
	col2 = dataTable.Columns["Well Name (Header)"].RowValues.GetFormattedValue(rowIndexSet.First)
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
	#OilIp is a document property
	data_for_new_row= str(col1) + "," + str(col2) + "," + str(Oil_IP)  + "," + str(Oil_B)  + "," + str(Oil_Di)  + "," + str(Oil_Dmin)  + "," + str(Oil_DaysFlat) + "," + str(Oil_Technical_EUR) + "," + str(Gas_IP) + "," + str(Gas_B)+ "," + str(Gas_Di)+ "," + str(Gas_Dmin)+ "," + str(Gas_DaysFlat)+ "," + str(Gas_Technical_EUR)+ "," + str(Cum_Oil_at_DaysFlat)+ "," + str(Cum) + "," + str(Months_Produced) + "," + str(Commercial_EUR) + "," + str(NPV10)+ "," + str(IRR) 
	textData = "API-14, Well Name (Header), Oil IP, Oil B, Oil Di, Oil Dmin, Oil Days Flat, Oil Technical EUR, Gas IP, Gas B, Gas Di, Gas Dmin, Gas Days Flat, Gas Technical EUR, Cum Oil at Days Flat, Cum, Months Produced, Commercial EUR, NPV-10, IRR\r\n" + data_for_new_row + "\r\n"

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
	textDataSource = TextFileDataSource(stream,readerSettings)
	settings = AddRowsSettings(dataTable,textDataSource)
	dataTable.AddRows(textDataSource,settings)