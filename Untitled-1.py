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

print("Would you like a list of the volunteers")
answer = input()
if answer == 'yes' or 'Yes':

    print(Person_01, Cointype_01)
    print(Person_02, Cointype_02)
    print(Person_03, Cointype_03)
    print(Person_04, Cointype_04)
    print(Person_05, Cointype_05)
    print(Person_06, Cointype_06)
else:
    print("Alright Fair Enough")
    
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

print("Would you like a complete list of the values and volunteers?")
answer_2 = input()
if answer_2 == 'yes' or 'Yes':
    print(Person_01, Cointype_01, Weight_1p)
    print(Person_02, Cointype_02, Weight_5p)
    print(Person_03, Cointype_03, Weight_20p)
    print(Person_04, Cointype_04, Weight_50p)
    print(Person_05, Cointype_05, Weight_1)
    print(Person_06, Cointype_06, Weight_2)
else:
    print("You Will See These Later On")

