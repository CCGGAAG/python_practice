import os
import shutil

# 选图确定的编号
dir = "E:\\单反随拍作品\\5月花怜\\新建文件夹"
copy_list = os.listdir(dir)
list1 = []
for i in copy_list:
    # print(str(i)[4:-4])
    list1.append(str(i)[0:-4])
print(list1)
print(len(list1))

# 所有的照片库
dir_raw = "E:\\单反随拍作品\\5月花怜\\raw"
all_list = os.listdir(dir_raw)
list2 = []
for j in all_list:
    # print(j)
    list2.append(str(j)[0:-4])
print(list2)
print(len(list2))

end_list = []
for x in list2:
    if x in list1:
        end_list.append(x)
print(end_list)
print(len(end_list))


for y in end_list:
    file1 = "E:\\单反随拍作品\\5月花怜\\raw\\" + y + ".CR2"
    file2 = "E:\\单反随拍作品\\5月花怜\\确认\\" + y + ".CR2"
    shutil.copy(file1, file2)
