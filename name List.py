names = []


n1= input("Enter a name: ")
names.append(n1)
n2= input("Enter second name: ")
names.append(n2)
n3= input("Enter third name: ")
names.append(n3)
n4= input("Enter forth name: ")
names.append(n4)
n5= input("Enter fifth name: ")
names.append(n5)
n6= input("Enter sixth name: ")
names.append(n6)
n7= input("Enter seventh name: ")
names.append(n7)
n8= input("Enter eighth name: ")
names.append(n8)
n9= input("Enter ninth name: ")
names.append(n9)
n10= input("Enter tenth name: ")
names.append(n10)


found = True

while found:
    search = input ("Enter a name to search for or 'End' to end the program: ")
    if search in names:
        print (search, "The name was found.")
        found = False
        break
    elif search == "End":
            found = False
    else:
        print(search, "The name was not found.")
        continue
    
