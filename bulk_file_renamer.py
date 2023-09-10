from os import listdir, rename
path = "bulk/"

newName = input("Enter new name: ")
c = 0

fileList = sorted(listdir(path))

for i in fileList:
    c+=1
    rename(f"{path}/{i}",f"{path}/{newName} {c}")
