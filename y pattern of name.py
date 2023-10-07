def printPattern(Str, Len):
    for i in range(Len):
        for j in range(Len):     
            if (i == j and i < Len/2-1 or (i + j == Len - 1)):
                print(Str[i], end="")       
            else:
                print("", end=" ")
        print()
Str = input()
Len = len(Str)
printPattern(Str, Len)
