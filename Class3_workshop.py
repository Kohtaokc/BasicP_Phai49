monster_hp = 50

weapon = {
    Gun = 10,
    Sword = 20,
    Punch = 30,
}


while True:
    print("1 = สู้ , 2 = หนี")
    Way = int(input("เลือกว่าจะสู้หรือไม่"))
    if Way == 2:
        print("runn!")
        break
    elif Way ==1:
        print("fight!")
    print("เลือกอาวุธของคุณ" 
    "Gun 10 Dmg",
    "Sword 20 Dmg",
    "Punch 30 Dmg")
    weapon = int(input("เลือกอาวุธ"))
    Round = int(input("ต้องการจะตีกี่รอบ"))
    for Round in range(1,4):
        totalDmg = weapon*round
        print("ดาเมจที่ทำได้" , totalDmg )