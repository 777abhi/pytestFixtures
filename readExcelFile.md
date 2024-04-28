### Read from Excel

1. **Using Pandas**:
   - First, make sure you have the `pandas` library installed. If not, you can install it using `pip install pandas`.
   - To read an Excel file as a DataFrame, use the `read_excel()` method. You can specify the path to the file and optionally the sheet name.
   - Example:
     ```python
     import pandas as pd
     df = pd.read_excel('sample.xlsx')  # Reads the first sheet by default
     print(df)
     ```
     This code reads the content of the Excel sheet and displays it as a DataFrame.

2. **Reading Specific Sheets**:
   - You can specify the sheet to read using the `sheet_name` argument. You can either specify the sheet index (starting at 0) or the sheet name.
   - Example (by sheet index):
     ```python
     df_sheet_index = pd.read_excel('sample.xlsx', sheet_name=1)  # Reads the second sheet
     print(df_sheet_index)
     ```
   - Example (by sheet name):
     ```python
     df_sheet_name = pd.read_excel('sample.xlsx', sheet_name='sheet2')  # Reads 'sheet2'
     print(df_sheet_name)
     ```

3. **Loading Multiple Sheets**:
   - You can also load multiple sheets into a dictionary-like structure using the `sheet_name` argument as a list.
   - Example:
     ```python
     df_sheet_multi = pd.read_excel('sample.xlsx', sheet_name=[0, 'sheet2'])
     print(df_sheet_multi[0])  # Access the first sheet
     print(df_sheet_multi['sheet2'])  # Access 'sheet2'
     ```

Remember to replace `'sample.xlsx'` with the actual path to your Excel file. Happy data manipulation! 📊🐍