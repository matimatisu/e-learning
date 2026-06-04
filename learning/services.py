import openpyxl

def grade_excel(file_path):

    workbook = openpyxl.load_workbook(file_path)#Excelファイルを開く

    sheet = workbook.active

    answer = sheet['B5'].value

    if answer == 600:

        return 100
    
    return 0
