import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Mango')
worksheet.write('A2', 'Orange')
worksheet.write('A3', 'Grapes')
worksheet.write('A4', 'Banana')

workbook.close()