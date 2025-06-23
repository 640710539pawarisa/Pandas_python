#สร้าง series จาก List & Tuple

import pandas as pd  #เรียกใช้งาน pandas เพื่อจัดการข้อมูล
import numpy as np  #เรียกใช้งาน numpy เพื่อจัดการข้อมูลของ array

#สร้าง list และ tuple

data_ls = [10,20,'Ae','10.05','ทุเรียน'] #สร้าง list #list คือ อาเรย์ที่สามารถเปลี่ยนได้   []
data_tp = (10,20,'Ae','10.05','ทุเรียน') #สร้าง tuple  #tuple คือ อาเรย์ที่ไม่สามารถเปลี่ยนได้ ()

#สร้าง series จาก list และ tuple เก็บไว้ในตัวแปร ชื่อ ps และ pt 

ps = pd.Series(data_ls) #สร้าง series จาก list
pt = pd.Series(data_tp) #สร้าง series จาก tuple

#แสดง series
print(ps ,"แบบ list")
print(pt ,"แบบ tuple") 