n=input("โปรดกรอกชื่อ\n")
a=input("โปรดกรอกอายุ\n")
i=input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
c=input("โปรดกรอกชั้นปี\n")
k=input("โปรดกรอกชื่อเล่น\n")
h=float(input("โปรดกรอกส่วนสูง\n"))
w=float(input("โปรดกรอกน้ำหนัก\n"))
A = h+w

print ("ชื่อ; " + n + " อายุ " + a + " ปี")
print ("รหัสประจำตัวนักศึกษา: " + i + " ระดับชั้น: " + c )
print ("ชื่อเล่น: " + k )
print ("ส่วนสูง: " + str(h) + " เชนติเมตร " + "น้ำหนัก: "+str(w) + "กิโลกรัม")
print ("ส่วนสูง + น้ำหนัก = " + str(A))
 