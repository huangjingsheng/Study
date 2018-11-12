import  xdrlib ,sys
import xlrd

#data = xlrd.open_workbook("D:/PyCharm-workspace/Uitest/配置文件.xlsx")
#table = data.sheet_by_name("driver")
#nrows = table.nrows
#print(nrows)
#colnames =  table.row_values(0)
#print(colnames)
#desired_caps = {}
driver = {}
def excel_table_byname():
     data = xlrd.open_workbook("D:/PyCharm-workspace/Uitest/配置文件.xlsx")
     table = data.sheet_by_name("Driver")
     #nrows = table.nrows#行数
     #row = table.row_values(rownum)
     #row = table.row_values(1)
     #print(row[0])
     #print(colnames)
     #range(1, nrows)，第一行到最后一行
     #len(row)，row 的长度
     #table.row_values(rownum)获取指定行的值
     """
     for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(row)):
                 app[colnames[i]] = row[i]
             list.append(app)
     return print(list)
    
     driver = {}
     for rownum in range(0, nrows+1):
         row = table.row_values(rownum)
         for i in range(len(row)):
             print(row[i])
     """
     for rownum in range(0, table.nrows):
         driver[table.cell(rownum,0).value] = table.cell(rownum,1).value
     return driver

driver = excel_table_byname()
print(driver)