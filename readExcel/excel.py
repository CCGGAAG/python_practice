# coding=utf-8
import xlwt
import  xdrlib ,sys
import xlrd
import pySQL
import time

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print (Exception)

def excel_table_byname(file= 'F:/pythonFile/全校学生联系方式.xlsx',colnameindex=1,sheet_name='Sheet1'):
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
             app = []
             for i in range(ncols):
                 app.append(row[i])
                # app[colnames[i]] = row[i]
             list.append(app)
    return list


def excel_get_valueFromTitle(list,colName,colValue):
    """  list : 列表         colName:列名      colValue列名值
          返回包含特定数据的一行（字典）
     """
    for row in list:
            if row[colName]== colValue:
                return row
               
                


def main():

   tables = excel_table_byname()
   for data in tables:
       try:
           sqls = "insert into student(department,major,class,name,sex,phone,phoneType) values('%s','%s','%s','%s','%s','%s','%s');"%(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
           print(sqls)
           pySQL.select(sqls)
           print(data)
       except:
           time.sleep(60)
           continue

if __name__=="__main__":
     main()
