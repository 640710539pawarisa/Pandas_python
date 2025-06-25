#การเข้าถึงข้อมูลใน series
#การเข้าถึงข้อมูลใน series ด้วย ตัวแปรชื่อ index และ ตัวแปรชื่อ value

import pandas as pd  #เรียกใช้งาน pandas เพื่อจัดการข้อมูล

#สร้าง series จาก dictionary
print("สร้าง series จาก dictionary")

#กลุ่มข้อมูลเก็บไว้ใน dictionary
data = {'องุ่น': 'grape' , 'กล้วย' : 'banana' ,'มะละกอ': 'papaya'} #//สร้าง dictionary

#สร้าง series จาก dictionary เพื่อ จัดการข้อมูล
ps = pd.Series(data) #สร้าง series จาก dictionary

#ลองแสดง series
print(ps)

print("---------------------------")
#การเข้าถึงข้อมูลใน series (อ้างอิง index ) 
#การระบุ index ในการเข้าถึงข้อมูล ในรุปแบบ ข้อความ

ps['องุ่น']
ps['กล้วย']

print(ps['องุ่น'])
print(ps['กล้วย'])

print("---------------------------")    

#หรือใช้เลย index
#การระบุ index ในการเข้าถึงข้อมูล ในรุปแบบ ตัวเลข

ps[0]
ps[1]

print(ps[0])
print(ps[1])

print("---------------------------")

# เข้าถึงค่าด้วยตำแหน่ง (position) อย่างปลอดภัยด้วย iloc
print(ps.iloc[0])  # องุ่น
print(ps.iloc[1])  # กล้วย

print("---------------------------")