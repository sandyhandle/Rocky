import sys
import random

print("Welcome to Password Generator")

print('Enter the value greater than 5 and less than 61')

length = int(input("Enter the password length: "))

if not 5 < length < 61:
    print("Try Again")
    sys.exit()
dic = []
symbols = bool(int(input("If you waant symbols (!@#$%^&*()+) type 1 or enter 0 : ")))
if symbols:
    dic.append("!@#$%^&*()+")

numbers = bool(int(input("If you waant numbers (1-9) type 1 or enter 0 : ")))
if numbers:
    dic.append("1234567890")

lowercase = bool(int(input("If you waant lowercase (a-z) type 1 or enter 0 : ")))
if lowercase:
    dic.append("qwertyuiopasdfghjklzxcvbnm")

uppercase = bool(int(input("If you waant uppercase (A-Z)type 1 or enter 0 : ")))
if uppercase:
    dic.append("QWERTYUIOPASDFGHJKLZXCVBNM")
    
otherSymbols = bool(int(input("If you waant other symbols (~`[];?,) type 1 or enter 0 : ")))
if otherSymbols:
    dic.append("~`[];?,")

print(dic)
ans = ""
for i in range(length):
    temp = random.choice(dic)
    ans += random.choice(temp)
print(ans)

# """
# Password Length 
# Allow Symbols (!@#$%^&*()+)
# Allow Numbers (0-9)
# Allow Lowercase (abc) 
# Allow Uppercase (ABC)
# Exclude Duplicate Characters 
# Allow Other Symbols (~`[];?,)
# """