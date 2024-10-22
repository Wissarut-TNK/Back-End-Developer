score =int(input("ใส่คะแนน :"))
if score < 0 or score > 100:
   print ('ใสเลข 0 - 100')
elif score >= 80:
   print("เกรด4")
elif score >= 70:
   print("เกรด3")
elif score >= 60:
   print("เกรด2")
elif score >= 50:
   print("เกรด1")
elif score >= 0:
   print("เกรด0")