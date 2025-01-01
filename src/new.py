def createlist():
    with open("test.txt", "r") as f:
        mylist = f.read()
    mylist = mylist.splitlines()
    # print(mylist)
    secondlist = []
    # for eintrag in mylist:
    #    secondlist.append(eintrag)
    # print(secondlist)
    print("mylist = [")
    for entry in mylist:
        print(f'    "{entry}",')
    print("]")


createlist()
