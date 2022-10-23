
import configparser


cursor =configparser.ConfigParser()


cursor.read("furkanconfig.cfg")
while True:
    cursor.read("furkanconfig.cfg")
    print(cursor["kisi_bilgiler"]["ismi"])




"""
a = open("furkan.txt","a")

pancar_kilosu = 20


#a.write("kilo={}\n".format(pancar_kilosu))
a.writelines("srfsfszfsfsfsfsfsfsfsx")


a.close()



t = a.readline()
print(t)
kilosu = 0
data = t.strip().split("=")
if (data[0] == "kilo"):
    kilosu = data[1]


print(kilosu)

a.close()
"""