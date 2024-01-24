import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)  #  Если исключений не возникает, блок except пропускается
                          #  программа продолжает выполнятся обычным образом
        print(entry, r)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()