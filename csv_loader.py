import os
import pandas as pd
from datetime import datetime
from tkinter import Tk, filedialog

#function that converts currency columns from strings to floats
def col_to_float(col):
    col = col.str[1:]
    col = col.str.replace(',', '')
    return pd.to_numeric(col)

file_path = filedialog.askopenfilename(
    title="Select your statement file",
    filetypes=[("Excel files", "*.xls *.xlsx"), ("All files", "*.*")]
)

# Read the HTML tables from the file, not sure why they are technically HTML, banks are weird
tables = pd.read_html(file_path)
raw = tables[0]

# Organise the data, removing unncessary rows and columns, renaming columns, and dropping empties
df = raw.iloc[4:]
df = df[[1, 3, 5, 6, 7]]
df.columns = "Date", "Description", "Money In", "Money Out", "Balance"
df = df.dropna(how="all")

# Convert the data to the correct types
date_format = '%d/%m/%Y'

df['Date'] = pd.to_datetime(df['Date'], format=date_format, errors='coerce')
df['Money In'] = col_to_float(df['Money In'])
df['Money Out'] = col_to_float(df['Money Out'])
df['Balance'] = col_to_float(df['Balance'])

# Save the cleaned data to a new Excel file
base, ext = os.path.splitext(file_path)
df.to_excel(f'{base}_cleaned.xlsx', index=False)