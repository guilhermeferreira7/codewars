def sing():
    bottles = ['']*200

    for i in range(200, -1, -1):
        print(i - 101)
        # bottles[i] = str(i - 100) + " bottles of beer on the wall, 99 bottles of beer. \n"
        # bottles[i-1] = str(i) + "Take one down and pass it around, 98 bottles of beer on the wall. \n"
    return bottles


print(sing())