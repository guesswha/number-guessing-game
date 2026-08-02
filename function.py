def chooseHardness():
    while True:
        try:
            hardness = int(input("\nChoose the hardness: "))
        
            if 1 <= hardness <= 3:
                break 
            else:
                print("Enter 1 or 2 or 3 to choose the hardness!")
            
        except ValueError:
            print("Enter 1 or 2 or 3 to choose the hardness!")
    if hardness == 1:
        return 10
    elif hardness == 2:
        return 7
    else:
        return 5