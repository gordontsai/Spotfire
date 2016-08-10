import clr
clr.AddReference('System.Data')
import System
from System.Data import DataSet, DataTable, XmlReadMode
from Spotfire.Dxp.Data import DataType, DataTableSaveSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from System.Threading import Thread
from Spotfire.Dxp.Data import IndexSet
from Spotfire.Dxp.Data import RowSelection
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Data import DataSelection
from Spotfire.Dxp.Data import DataPropertyClass
from Spotfire.Dxp.Data import Import
from System import DateTime
from System import DateTime, TimeSpan, DayOfWeek
from datetime import date
from System.Net import HttpWebRequest
import time
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import AddRowsSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import AddColumnsSettings, JoinType, DataColumnSignature, DataType
from Spotfire.Dxp.Data.Import import DataTableDataSource


Daily_Header =  Document.Data.Tables["Daily Header"]
DCA_Parameters = Document.Data.Tables["DCA Parameters"]
# Remove Rows from DCA Parameter Table
#rowCount = DCA_Parameters.RowCount
#print rowCount
#rowsToRemove = IndexSet(rowCount, True)
#print rowsToRemove
#DCA_Parameters.Column(RowSelection(rowsToRemove))
#DCA_Parameters.Columns.Remove("API-14")
#DCA_Parameters.Columns.Remove("Well Name (Header)")


rowCount = Daily_Header.RowCount
rowsToInclude = IndexSet(rowCount,True)
API_List = DataValueCursor.CreateFormatted(Daily_Header.Columns["API-14"])
Well_List = DataValueCursor.CreateFormatted(Daily_Header.Columns["Well Name (Header)"])


### Create join dictionary
ColumnA = DataColumnSignature(Daily_Header.Columns["API-14"])
ColumnB = DataColumnSignature(DCA_Parameters.Columns["API-14"])
ColumnC = DataColumnSignature(Daily_Header.Columns["Well Name (Header)"])
ColumnD = DataColumnSignature(DCA_Parameters.Columns["Well Name (Header)"])

joinConditionMap = {ColumnA : ColumnB, ColumnC : ColumnD}
#Creating Data table Source to be used as the column frmo which we're pulling data to add
ds = DataTableDataSource(Daily_Header)
#dataSource = DataTableDataSource(Daily_Header)
#flowBuilder = DataFlowBuilder(dataSource, Application.ImportContext)
#sourceReader = flowBuilder.Execute(DataSourcePromptMode.None)
ignoredCols =[]

#ignoredCols = [DataColumnSignature(sourceReader.Columns["Latitude"])]


#for column in Document.Data.Tables["Daily Header"].Columns:
#	if not column.Name == "API-14" and not column.Name == "Well Name (Header)"
#		ignoredCols.append(DataColumnSignature(column))


#for col in Daily_Header.Columns:
#		if not colNamesToAddArrayList.Contains(col.Name) and not rightColsArrayList.Contains(col.Name) :
#			try:
#				print "INFO: Ignoring: " + col.Name + " in join"
#				ignoreCols.Add(DataColumnSignature(sourceReader.Columns[col.Name]))
#			except:
#				#Column doesn't exist??
#				print "WARN: Error trying to ignore column " + col.Name + " from " + rightTable.Name + "! Maybe it doesn't exist??"





settings = AddColumnsSettings(joinConditionMap, JoinType.RightOuterJoin, ignoredCols)
DCA_Parameters.AddColumns(ds, settings)



#Document.Data.Tables["DCA Parameters"].Columns.Clear("API-14")
#Document.Data.Tables["DCA Parameters"].Columns.Clear("Well Name (Header)")



#for row in Daily_Header.GetRows(rowsToInclude) :
#	if 


#registration = DataValueCursor.CreateFormatted(Document.Data.Tables[].Columns["Registration ID"])

#AddColumnsSettings( joinConditionMap, JoinType.LeftOuterJoin, ignoredCols)