import xlrd
import xlwt
# import

def read_excel():
    file_path=r'F:\gitroot\Autoproject\data\data.xlsx'

    workbook = xlrd.open_workbook(file_path)    #实例化工作簿对象
    sheet_names = workbook.sheet_names()    #获取所有工作表的名字
    print('获取所有工作表的名字',sheet_names)
    sheet = workbook.sheet_by_name('register')
    rows=sheet.nrows
    cols=sheet.ncols
    print('总行数=',rows,'总列数=',cols)
    #遍历所有行内容
    content=[]
    for line in range(1,rows):
        lines=sheet.row_values(line,0,4)
        lines[3] = str(int(lines[3]))
        content.append(lines)
        print('行内容',lines)

    return content

content=read_excel()
print('读取成功',content)

# def read_csv():