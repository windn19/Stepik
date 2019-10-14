import xlrd


work = xlrd.open_workbook('price_russia.xls')
sheet = work.sheet_by_index(0)
for i in range(18, sheet.nrows):
    data = sheet.row(i)
    print(data)
