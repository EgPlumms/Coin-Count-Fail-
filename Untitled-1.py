print("""
  ______             __                   ______                                   __     
 /      \           /  |                 /      \                                 /  |    
/$$$$$$  |  ______  $$/  _______        /$$$$$$  |  ______   __    __  _______   _$$ |_   
$$ |  $$/  /      \ /  |/       \       $$ |  $$/  /      \ /  |  /  |/       \ / $$   |  
$$ |      /$$$$$$  |$$ |$$$$$$$  |      $$ |      /$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$/   
$$ |   __ $$ |  $$ |$$ |$$ |  $$ |      $$ |   __ $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ | __ 
$$ \__/  |$$ \__$$ |$$ |$$ |  $$ |      $$ \__/  |$$ \__$$ |$$ \__$$ |$$ |  $$ |  $$ |/  |
$$    $$/ $$    $$/ $$ |$$ |  $$ |      $$    $$/ $$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ 
 $$$$$$/   $$$$$$/  $$/ $$/   $$/        $$$$$$/   $$$$$$/   $$$$$$/  $$/   $$/    $$$$/  """)

print("Who is the first volunteer?")
Person_01 = input()
print("What coin did they count?")
Cointype_01 = input()

print("Who is the second volunteer?")
Person_02 = input()
print("What coin did they count?")
Cointype_02 = input()

print("Who is the thrid volunteer?")
Person_03 = input()
print("What coin did they count?")
Cointype_03 = input()

print("Who is the fourth Volunteer?")
Person_04 = input()
print("What coin did they count?")
Cointype_04 = input()

print("Who is the Fith Volunteer?")
Person_05 = input()
print("What coin did they count?")
Cointype_05 = input()

print("Who is the Final Volunteer?")
Person_06 = input()
print("What coin did they count?")
Cointype_06 = input()

answer = input("Would you like a list of the volunteers?")
if answer == 'yes' or answer == 'Yes':
    print("Volunteers:", Person_01,Person_02,Person_03,Person_04,Person_05,Person_06)
    print("Cointype:", Cointype_01,Cointype_02,Cointype_03,Cointype_04,Cointype_05,Cointype_06)
else:
    print("You Will See This Later On")
    
print("What is the weight of the 1p bag?")
Weight_1p = input()
print("What is the weight of the 5p bag?")
Weight_5p = input()
print("What is the weight of the 20p bag?")
Weight_20p = input()
print("What is the weight of the 50p bag?")
Weight_50p = input()
print("What is the weight of the £1 bag?")
Weight_1 = input()
print("What is the weight of the £2 bag?")
Weight_2 = input()

answer_2 = input("Would you like a complete list of the values and volunteers?")
if answer_2 == 'yes':
    print("Volunteers:", Person_01,Person_02,Person_03,Person_04,Person_05,Person_06)
    print("Cointype:", Cointype_01,Cointype_02,Cointype_03,Cointype_04,Cointype_05,Cointype_06)
    print("Weight(g)", Weight_1p,Weight_5p,Weight_20p,Weight_50p,Weight_1,Weight_2)

elif answer_2 == 'Yes':
    print("Volunteers:", Person_01,Person_02,Person_03,Person_04,Person_05,Person_06)
    print("Cointype:", Cointype_01,Cointype_02,Cointype_03,Cointype_04,Cointype_05,Cointype_06)
    print("Weight(g)", Weight_1p,Weight_5p,Weight_20p,Weight_50p,Weight_1,Weight_2)
else:
    print("You Will See These Later On")

Value_1 = input("What Is The Bag Value Of ",Cointype_01)
Value_2 = input("What Is The Bag Value Of ",Cointype_02)
Value_3 = input("What Is The Bag Value Of ",Cointype_03)
Value_4 = input("What Is The Bag Value Of ",Cointype_04)
Value_5 = input("What Is The Bag Value Of ",Cointype_05)
Value_6 = input("What Is The Bag Value Of ",Cointype_06)

Total_1 = Value_1 * Weight_1p
Total_2 = Value_2 * Weight_5p
Total_3 = Value_3 * Weight_20p
Total_4 = Value_4 * Weight_50p
Total_5 = Value_5 * Weight_1
Total_6 = Value_6 * Weight_2

