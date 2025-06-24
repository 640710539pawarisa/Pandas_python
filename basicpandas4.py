#สร้าง Series จาก Dictionary
#คล้าย ๆ basicpandas3.py 

#ตัวอย่างการสร้าง dictionary *******
#โครงสร้างจะมี key และ value
# ชื่อตัวแปรที่จะใช้เก็บ dictionary = {key : value}
#เช่น
# sum = {'ชื่อ': 'ค่า'}
#แบบอื่นๆเช่น list และ tuple จะเป็น sum = [ชื่อ , ค่า] และ sum = (ชื่อ , ค่า)

import pandas as pd  #เรียกใช้งาน pandas เพื่อจัดการข้อมูล

#สร้าง dictionary
print("ข้อมูล ใน dictionary")
data = {'องุ่น': 50 ,'อาหาร' : 20,'เครื่องดื่ม' : 30,'อื่นๆ': 10} #สร้าง dictionary
print(data) #แสดง dictionary

print("---------------------------")

#สร้าง series จาก dictionary
print("สร้าง series จาก dictionary")

ps = pd.Series(data) #สร้าง series จาก dictionary

#แสดง series
print(ps)

print("---------------------------")

#หรือ สร้าง dictionary จับคู่สี
colors = {'สีดํา' : 'black','สีแดง' : 'red','สีเหลือง' : 'yellow','สีเขียว' : 'green'}

#แสดง ข้อมูลใน colors
print(colors)

print("---------------------------")

#สร้าง Series จาก dictionary จับคู่สี
print("สร้าง series จาก dictionary จับคู่สี")

ps = pd.Series(colors) #สร้าง series จาก dictionary

#แสดง series
print(ps)

print("---------------------------")

#ลองสร้าง dictionary จับคู่ชื่อกับ อายุ
age = {'เอ๊ะ ':22,'โคล่า ' : 1 ,'เซเว่น': 1 }

#แสดง ข้อมูลใน age
print(age)

print("---------------------------")

#สร้าง Series จาก dictionary จับคู่ชื่อกับ อายุ
print("สร้าง series จาก dictionary จับคู่ชื่อกับ อายุ")

ps = pd.Series(age) #สร้าง series จาก dictionary

#แสดง series
print(ps)   

print("---------------------------")