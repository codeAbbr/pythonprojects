import random


print("************* Run code to generate a password *************")

# Password Length

passwordLength = int(input("Input password lenght: "))

# Letters


small_letters_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

small_letters = "".join(small_letters)


capital_letter = "".join(small_letters).upper()


# Numbers

numbers = ["1","2","3","4","5","6","7","8","9","10"]


convert_number = "".join(numbers)


characterList = small_letters + capital_letter + convert_number




newPasswordList = []



for i in range(passwordLength):
    newPasswordList.append(random.choice(characterList))
    
    random.shuffle(newPasswordList)
    

print("New Password: " + "".join(newPasswordList))