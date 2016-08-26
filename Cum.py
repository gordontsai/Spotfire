#Cum To Date
from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import AddColumnsSettings, JoinType, DataColumnSignature, DataType
from Spotfire.Dxp.Data.Import import DataTableDataSource
from Spotfire.Dxp.Data import DataValueCursor

dataTable = Document.Data.tables["Oxy Eag Daily Production"].AsIndexSet()

rowIndexSet = Document.Data.Markings["Marking"].GetSelection(dataTable).AsIndexSet()


Cum = max(dataTable.Columns["Cum Oil"].RowValues.GetValue(rowIndexSet))

print Cum