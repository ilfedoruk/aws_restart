import math

def matrix ():
    
    size = input("Enter a number: ")
    if size.isnumeric () ==True:
        size = int(size)
        print("Identity matrix")
        for row in range (0, size):
            for col in range (0, size):
                if (row == col):
                    print("1 ", end=" ")
                else:
                    print ("0 ", end=" ")
            print ()
    else:
        print ("It's not a number!")
        
print (matrix())