from os import listdir, rename
path = "bulk/"

to_be_replaced = input("String to be replaced: ")
replacement = input("Replacement: ")

c = 0

fileList = sorted(listdir(path))

for i in fileList:
    c+=1
    name = f"{path}/{i}"
    rename(name, name.replace(to_be_replaced, replacement))
# THANKS FOR WATCHING

