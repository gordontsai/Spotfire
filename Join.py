from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import AddColumnsSettings, JoinType, DataColumnSignature, DataType
from Spotfire.Dxp.Data.Import import DataTableDataSource

ColumnA = DataColumnSignature(Document.Data.Tables["Daily Header"].Columns["API-14"])
ColumnB = DataColumnSignature(Document.Data.Tables["DCA Parameters"].Columns["API-14"])
Column_IP = Application.Document.Data.Tables["DCA Parameters"].Columns["B Factor"].Name
print Column_IP
joinConditionMap = {ColumnA : ColumnB}
ignoredCols = []

#Remove IP Column
if Column_IP == Application.Document.Data.Tables["Daily Header"].Columns["B Factor"].Name:
	Document.Data.Tables["Daily Header"].Columns.Remove("B Factor")

#Remove B Value Column
#if Column_IP == Application.Document.Data.Tables["Daily Header"].Columns["IP"].Name:
	#Document.Data.Tables["Daily Header"].Columns.Remove("IP")

settings = AddColumnsSettings( joinConditionMap, JoinType.LeftOuterJoin, ignoredCols)
ds = DataTableDataSource(Document.Data.Tables["DCA Parameters"])
Document.Data.Tables["Daily Header"].AddColumns(ds, settings)
Document.Data.Tables["Daily Header"].Columns.Remove("Well Name (Header) (2)")

#this code joins columns from BakkenWells to Normalized Monthly Data