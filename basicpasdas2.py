#สร้าง Series จาก Numpy (nArray)

import pandas as pd  #เรียกใช้งาน pandas เพื่อจัดการข้อมูล
import numpy as np  #เรียกใช้งาน numpy เพื่อจัดการข้อมูลของ array

#สร้าง numpy array และ series จาก numpy array เก็บไว้ในตัวแปร ชื่อ data_ls 

data_ls = [10,20,'Ae','10.05','ทุเรียน'] #สร้าง list #list คือ อาเรย์ที่สามารถเปลี่ยนได้   []

#สร้าง series จาก numpy array 

ndata = np.array(data_ls) #สร้าง numpy array
ps = pd.Series(ndata) #สร้าง series จาก numpy array เก็บไว้ในตัวแปร ชื่อ ps 

#หรือ แบบไม่เก็บในตัวแปร ชื่อ ps ก็ได้
print("แบบไม่เก็บในตัวแปร ชื่อ ps ")
print(pd.Series([10,20,'Ae','10.05','ทุเรียน']))
print("---------------------------")

#หรือ สร้างใน บรรทัดเดียวก็ได้ และแสดง ในบรรทัดเดียว 
print("แบบ สร้างใน บรรทัดเดียว")
ndata2 = np.array([10,20,'Ae','10.05','ทุเรียน',True])
print(pd.Series(ndata2)) #สร้าง series จาก numpy array
print("---------------------------")

#แสดง series
print("แสดง series แบบ เก็บในตัวแปร ชื่อ ps")
print(ps)
print("---------------------------")
