# coding=utf-8
import xlrd
import xlwt

#data = xlrd.open_workbook("../data/abc.xlsx")
#table =data.sheet_sheet_index("a")
#print(table.cell(0,0).value)
#print(table.ncols)
#print(table.row_values(0))
# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print (Exception)
        

def excel_table_byindex(file= 'file.xls',colnameindex=0,sheet_index=0):
    """根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，sheet_index：表的索引"""
    data = open_excel(file)
    table = data.sheets()[sheet_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list


def excel_table_byname(file= '../test_data/abc.xlsx',colnameindex=0,sheet_name='Sheet1'):
    """根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，sheet_index：Sheet1名称"""
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows #行数 
    ncols =table.ncols      #列数    
    
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(ncols):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


def excel_get_valueFromTitle(list,colName,colValue):
    """  list : 列表         colName:列名      colValue列名值
          返回包含特定数据的一行（字典）
     """
    for row in list:
            if row[colName]== colValue:
                return row
               
                
#     
#    data = xlrd.open_workbook("../data/abc.xlsx")
#    table = data.sheet_by_name("a")
#    nrows = table.nrows #行数 
#    ncols =table.ncols      #列数
#    print(nrows)
#    print(ncols)
#    
#    
#    colnames =  table.row_values(0) #某一行数据 
#    list =[]
#    for rownum in range(1,nrows):
#         row = table.row_values(rownum)
#         if row:
#             app = {}
#             for i in range(ncols):
#                app[colnames[i]] = row[i]
#             list.append(app)
#    print(list)
#    print("-------------------")
#    for row in list:
#            if row['Casename']=='loginTest':
#                print(row["Value"])



def main():
   tables = excel_table_byindex()
   for row in tables:
       print (row)

   tables = excel_table_byname()
   for row in tables:
       print (row)

if __name__=="__main__":
    main()