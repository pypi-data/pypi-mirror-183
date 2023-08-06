# xlsxopera
Working on xlsx (Microsoft Excel) files. Convert to list, dict, get headers, cell values, positions and more.

Developed by voidayan (c) 2022

## Install

Install package from pip:
```
pip3 install xlsxopera
```
Note: Required packages is openpyxl
## How to work

Create an object

```python
from xlsxopera import Notebook

# Load file to operate and sheet name
notebook = Notebook("file-to-path.xlsx", "sheet_name")
# Or load file to operate without sheet name. Default will be active spreadsheet.
notebook = Notebook("file-to-path.xlsx")
```

Get rows in list of lists:
```python
# Get all rows (from 1 to last)
rows_in_spreadsheet = notebook.list_rows()
# Get rows (for e.g, from 9 to 13)
rows_in_spreadsheet = notebook.list_rows(start=9, end=13)
```
