#สร้าง Series แบบกำหนดหมายเลข index 
#ปกติ การสร้าง Series จะมีหมายเลข index อัตโนมัติ แต่เราสามารถกําหนดหมายเลข index ได้ *****

#เรื่องนี้ ไม่ได้ใช้เรื่อง Numpy เลย 
import pandas as pd  #เรียกใช้งาน pandas เพื่อจัดการข้อมูล

items = ['มะม่วง','มะละกอ','กล้วย','ส้ม'] #สร้าง list

#แสดง ชุดข้อมูล ใน list
print("ชุดข้อมูล ใน list ")
print(items)

print("---------------------------")

#สร้าง series จาก list แบบไม่กําหนดหมายเลข index
print("สร้าง series จาก list แบบไม่กําหนดหมายเลข index")
ps = pd.Series(items) #สร้าง series จาก list
print(ps) 

print("---------------------------")

#ถ้าอยากกําหนดหมายเลข index ละ 50,20,30,40
#สร้างตัวแปรมาเก็บ index ที่ต้องการ
idx = [50,20,30,40]

#แสดง index
print("แสดง index ที่เราต้องการกำหนด")
print(idx)

print("---------------------------")

#สร้าง series จาก list และกําหนดหมายเลข index ได้
print("สร้าง series จาก list และกําหนดหมายเลข index ได้")
ps = pd.Series(items,index = idx) 

#สร้าง series จาก list , pd.Series(ชุดข้อมูล,กําหนดหมายเลขindex 

#แสดง series 
print(ps)

print("---------------------------")

#สร้าง series จาก list , pd.Series(ชุดข้อมูล,กําหนดหมายเลขindex )

