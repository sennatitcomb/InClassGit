def divisor(a):
   for i in range (1, a+1):
        if (a % i == 0):
            print(i)

divisor(int(input("Enter a number: ")))