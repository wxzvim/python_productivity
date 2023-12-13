import openpyxl
import os

src_file = "./salary-list.xlsx"
print(os.getcwd())

workbook = openpyxl.load_workbook(src_file)
sheet = workbook.active
cell_header = [cell.value for cell in sheet[1]]
print(cell_header)
