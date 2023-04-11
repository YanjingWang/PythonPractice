# import win32com.client
# from PIL import ImageGrab

# # specify the path to your Excel file here
# excel_file_path = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard\Citywide.xlsx'

# # specify the path to your PowerPoint file here
# powerpoint_file_path = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard\Citywide RS Powerpoint.pptm'

# # open the Excel file
# xlapp = win32com.client.Dispatch("Excel.Application")
# wb = xlapp.Workbooks.Open(excel_file_path)
# sheet = wb.Sheets(1)

# # take a screenshot of the data from column A to column C, row 1 to row 4
# screenshot = ImageGrab.grabclipboard()
# screenshot.save('screenshot.png')

# # open the PowerPoint file
# ppapp = win32com.client.Dispatch("PowerPoint.Application")
# ppapp.Visible = True
# presentation = ppapp.Presentations.Open(powerpoint_file_path)

# # paste the screenshot into the first slide of the presentation
# slide = presentation.Slides(1)
# slide.Shapes.AddPicture('screenshot.png', False, True, 100, 100)

# # save and close the PowerPoint file
# presentation.Save()
# presentation.Close()

# # close the Excel file
# wb.Close(False)
# xlapp.Quit()


import win32com.client
import pythoncom

# specify the path to your Excel file here
excel_file_path = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard\Citywide.xlsx'

# specify the path to your PowerPoint file here
powerpoint_file_path = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard\Citywide RS Powerpoint.pptm'

# open the Excel file
xlapp = win32com.client.Dispatch("Excel.Application")
wb = xlapp.Workbooks.Open(excel_file_path)
sheet = wb.Sheets(1)

# copy the data from column A to column C, row 1 to row 4 as a picture
sheet.Range("A21:D31").CopyPicture(Appearance=1, Format=2)

# create a temporary chart object and paste the picture into it
chart = sheet.ChartObjects().Add(0, 0, 400, 300)
chart.Chart.Paste()
chart.Chart.Export('screenshot.png')
chart.Delete()

# open the PowerPoint file
ppapp = win32com.client.Dispatch("PowerPoint.Application")
ppapp.Visible = True
presentation = ppapp.Presentations.Open(powerpoint_file_path)

# paste the screenshot into the first slide of the presentation
slide = presentation.Slides(1)
slide.Shapes.AddPicture('screenshot.png', False, True, 100, 100)

# save and close the PowerPoint file
presentation.Save()
presentation.Close()

# close the Excel file
wb.Close(False)
xlapp.Quit()
