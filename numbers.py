print("Enter a number:")


def showNumbers(limit):
    for x in range(limit + 1):
        if x % 2 == 0:
            print(f"{x} EVEN")
        else:
            print(f"{x} ODD")


showNumbers(int(input()))
