#How to identify a leap year


n = int(input("Enter the Year n:"))
if (n % 4 == 0)and (n % 100 == 0) and(n % 400 == 0 ):
    print("leap year")

else :
    print("Not a leap year")
