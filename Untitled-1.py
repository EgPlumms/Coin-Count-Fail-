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


