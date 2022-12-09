class MultiplyTable():
    def table(n):
        for i in range(2,n+1): 
            print("\nMultiplication table for ",i)
            for j in range(1,11):
                print(i,"x",j ,"=",i*j)

n=int(input("Enter the value for the table :"))

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|  Multiplication Tables till the Entered value |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

MultiplyTable.table(n)
