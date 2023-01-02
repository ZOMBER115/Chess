
import string
numeros = "    1    2    3    4    5    6    7    8    "

print(numeros)
for i in range(8):

    print(string.ascii_lowercase[i],end=" ")
    for j in range(8):

        if((j+1+i)%2 == 0):
            print(" +++ ",end="")
        else:
            print(" *** ",end="")
    print(string.ascii_lowercase[i])
print(numeros)