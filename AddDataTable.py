##Using an IronPython script to add a data table with a Pivot transformation.


#Description: The following example illustrates how to add a data table with a Pivot transformation using an Iron Python script.

#Resolution: from Spotfire.Dxp.Data import DataFlowBuilder, DataColumnSignature, DataType, DataSourcePromptMode

from Spotfire.Dxp.Data.Transformations import PivotTransformation

from System.Collections.Generic import List

from Spotfire.Dxp.Data.Import import DataTableDataSource

table = Document.Data.Tables['TestData']

ds = DataTableDataSource(table)

ds.IsPromptingAllowed = False

ds.ReuseSettingsWithoutPrompting = True

dfb = DataFlowBuilder(ds, Application.ImportContext)

pivot = PivotTransformation()

list = List[DataColumnSignature]()

list.Clear()

col = table.Columns['Random']

list.Add(DataColumnSignature(col))

pivot.IdentityColumns = list

# Category columns.

#col = table.Columns['Active']

#list.Add(DataColumnSignature(col))

#col = table.Columns['County']

#list.Add(DataColumnSignature(col))

#pivot.CategoryColumns = list

dfb.AddTransformation(pivot)

flow = dfb.Build()

Document.Data.Tables.Add("nip",flow)

Disclaimer: