monster_hp = 50
att_round = 0


while True:
    print("1 = สู้ , 2 = หนี")
    Way = int(input("เลือกว่าจะสู้หรือไม่ "))
    if Way == 2:
        print("runn!")
        break
    elif Way ==1:
        print("fight!")
    print("อาวุธของคุณ"
    "1 = Gun 10 Dmg",
    "2 = Sword 20 Dmg",
    "3 = Punch 30 Dmg")
    print("เลือดของบอส", monster_hp )
    print("โจมตีได้สูงสุด 3 รอบ")
    att_round = int(input("ต้องการโจมตีกี่รอบ 1 2 หรือ 3"))   
    
    
    if 0 < att_round <= 3: 
            print("คุณต้องโจมตี :" ,int (att_round) , "โปรดเลือกอาวุธของคุณ")
    wea = int(input("อาวุธ"))
    
    for i in range(att_round): #กรอกได้ทีละ 1 รอบ
        if wea == 3:
            monster_hp = monster_hp - 30
            att_round = att_round - 1
            print("30ดาเมจสู่บอส",)
            print("บอสเหลือHP" , monster_hp)
            print("โอกาสโจมตีมีอีก", att_round)
        elif wea == 2:
            att_round = att_round - 1
            monster_hp = monster_hp - 20
            print("20ดาเมจสู่บอส",)
            print("บอสเหลือHp",monster_hp)
            print("โอกาสโจมตีมีอีก", att_round)
        elif wea == 1:
            att_round = att_round - 1
            monster_hp = monster_hp - 10
            print("10ดาเมจสู่บอส",)
            print("บอสเหลือHp" , monster_hp)
            print("โอกาสโจมตีมีอีก", att_round)
        else:
            print("ไม่เลือกอาวุธ")
    if att_round == 0:

        if monster_hp == 0:
            print("your winn!!!!")
            break
        elif monster_hp < 0:
            print("โปรดโจมตีให้บอสHpเหลือ 0 ")
            print("บอสคืนชีพพ!!!!")
            monster_hp = 20
            print("มอนสเตอร์ฟื้นคืนชีพ! มี HP เหลือ:", monster_hp)
