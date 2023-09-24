print("********** REGISTRATION CONSOLE APPLICATION ***********")
# Enter only words
username = str(input("Input username please: "))
# Enter only words
password = str(input("Input password please: "))
# username must not be less than or greater 10
if len(username) < 10 or len(username) > 10:
    print("Username is greater and less than 10")
# password must not be less than or greater 10
if len(password) < 10 or len(password) > 10:
    print("Password is greater and less than 10")
    
# username and password must be 10
if len(username) == 10 and len(password) == 10:
    success = 'Username: {}, Password: {}'.format(username,password)
    print("----------- Login Sucessful -------------------")
    with open("login_info.txt","a") as file:
        file.write('\n' +success)

# Reading 'login_info.txt' file
option = input("Do you want to view login info file ?")
if option == "yes":
    with open("login_info.txt","r") as file:
        print(file.readlines())
else:
    print("Run file to register again.")
    