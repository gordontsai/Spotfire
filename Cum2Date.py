
activeFilteringSelection = Document.Data.Markings["Marking"].GetSelection(myTable).AsIndexSet()
column = myTable.Columns["Cum Oil"]

max = column.RowValues.GetMaxValue(activeFilteringSelection).ValidValue/1000

Document.Properties["Cum2Date"] = max

print Document.Properties["Cum2Date"]