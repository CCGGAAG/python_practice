import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("test")
ws.write()
wb.save("tests.xlsx")