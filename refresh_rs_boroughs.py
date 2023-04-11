import os
import glob
import shutil
import base64
import requests
import datetime
import time
from datetime import date
from ms_graph import generate_access_token
import win32com.client as win32
import subprocess
# from rpy2 import robjects
import win32com.client


# def refresh_pivot_tables(file_path):
#     # Start Excel application
#     excel = win32com.client.Dispatch("Excel.Application")
#     # Set to False if you want the Excel application to run in the background
#     excel.Visible = True
#     # Open the workbook
#     wb = excel.Workbooks.Open(file_path)
#     # Refresh all data connections
#     for connection in wb.Connections:
#         connection.Refresh()
#     # Wait for a while to allow the data connections to refresh
#     time.sleep(10)
#     # Refresh all pivot tables
#     for ws in wb.Worksheets:
#         for pivot in ws.PivotTables():
#             pivot.PivotCache().Refresh()
#     # Wait for a while to allow the pivot tables to refresh
#     time.sleep(10)
#     # Save and close the workbook
#     wb.Save()
#     wb.Close()
#     # Quit the Excel application
#     excel.Quit()


# file_path = "\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard\Access Schools.xlsx"
# refresh_pivot_tables(file_path)


import os
import win32com.client

# specify the folder path here
folder_path = "\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard"

for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        xlapp = win32com.client.DispatchEx("Excel.Application")
        wb = xlapp.Workbooks.Open(Filename=file_path)
        wb.RefreshAll()
        for sheet in wb.Sheets:
            for pivot_table in sheet.PivotTableWizard():
                pivot_table.RefreshTable()
        wb.Save()
        xlapp.Quit()
