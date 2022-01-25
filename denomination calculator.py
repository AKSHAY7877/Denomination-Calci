
#Denominations calculator using 2000, 500, 200, 100 Notes By Akshay Sharma

print("Enter the Amount (ending with 00): ",end="")
amount = int(input())
two_thousand = int(amount / 2000)
five_hundred = int(amount % 2000 / 500)
two_hundred = int(amount % 2000 % 500 / 200)
hundred = int(amount % 2000 % 500 % 200 / 100)
print("Two thousand Rupee notes are : ",two_thousand)
print("Five Hundred Rupee notes are : ",five_hundred)
print("Two Hundred Rupee notes are : ",two_hundred)
print("Hundred Rupee note is ", hundred)