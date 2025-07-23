hasrice = True
hasspoon = False

if hasrice and hasspoon:
    print("มีช้อนมีข้าว")
 
if hasrice:
    print("มีข้าว")  #nested if
    if hasspoon:
        print("มีช้อน")
        print("can kinkao")
    else:
        print("kinkao mai dai mai me spoon")
else:
    print("cant kinkao")    
    
#Loop ลูป



for me_meaw in range(10):
    print("hi")

for i in range(5):
    print("hello",i + 1)

box = 0
for i in range(10):
    box = box + i #or box += i
print("ค่าของBox",box)

# วน 5 

spin = 5

boxie = 0

for i in range(1,5 + 1):
    boxie += i
    print('รอบที่ :',i ,"ผลรวมคือ :",boxie)

#inf loop

while True:
    inp = float(input(7))
    if inp == 7.0:
        break


i = 0 
while i < 5:
    i+=1
    print(i)
    
    
