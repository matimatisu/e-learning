import openpyxl
from .models import Assignment

def grade_excel(file_path, lesson):

    assignment = Assignment.objects.get(lesson = lesson) #DBのAssignmentを取ってくる

    formula_book = openpyxl.load_workbook(file_path)#関数の値を取得

    value_book = openpyxl.load_workbook(file_path,data_only=True)#関数を実行した結果の数値を取得

    #関数の判定
    required = assignment.required_formula.upper() #大文字化

    formula_sheet = formula_book.active #セル取得の実行

    formula = formula_sheet[assignment.answer_cell].value #answer_cellで指定したセルの値をとってくる

    formula = (formula.upper().replace(" ", ""))

    #投稿者が空欄で提出したときの保険
    if formula is None:
        
        return 0
    
    expected = (assignment.required_formula.upper().replace(" ", ""))

    value_sheet = value_book.active
    
    value =value_sheet[assignment.answer_cell].value #値を代入します

    formula_ok = (formula == expected) #関数を使用したかの確認

    value_ok = (str(value) == assignment.correct_value) #DBの答えの値と同じか確認

    if formula_ok and value_ok:
        
        return 100
    
    return 0


    
