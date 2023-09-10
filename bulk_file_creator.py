path = "bulk/"

length = input("Enter the number of files: ")

for i in range(int(length)):
    with open(f"{path}File {i}", "w") as file:
        pass