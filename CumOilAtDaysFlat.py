from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *


dataTable = Document.Data.Tables["Oxy Eag Daily Production"]
rowIndexSet=Document.ActiveMarkingSelectionReference.GetSelection(dataTable).AsIndexSet()
cursor = DataValueCursor.CreateFormatted(dataTable.Columns["Cum Oil At Days Flat"])




for c in dataTable.GetRows(rowIndexSet, cursor):
	print c.Index
		
