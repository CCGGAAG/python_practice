a = "¥148.00"
print(a.find("¥"))
b = a.find("¥")
c = a.find(".")
print(int(a[b+1:c])+10000)

aa = "237人在学"
print(aa.find("在学"))
d = aa.find("人")
print(aa[:d])