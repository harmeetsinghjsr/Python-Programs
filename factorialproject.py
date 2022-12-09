#1. Using for loop
n=int(input("Enter a number "))
i=1
f=1
for i in range(1,n+1):
    f*=i
print("factorial using for=",f)    
print()



#2. Using while loop
n=int(input("Enter a number "))
i=1
f=1
while(i<=n):
    
    f*=i
    i+=1
print("factorial using while loop=",f)    
print()




#3 no return no arg
def fact():
    a=int(input())
    fact=1
    for i in range(1,a+1):
        fact*=i;
    print("Factorial no return no args",fact)
        
    




#4 no return yes args
n=int(input())
def fact(n):
    f=1
    if n==0:
        print("Fcatorial:",1);
    else:
        for i in range(1,n+1):
            f*=i
        print("Factorial no return yes args:",f);



#5
n=int(input())
def fact(n):
    f=1
    if n==0:
        print("Fcatorial:",1);
    else:
        for i in range(1,n+1):
            f*=i
        return f;
o=fact(n)
print("Factorial yes return yes args:",o);





#6 yes return no args
def fact():
    a=int(input())
    f=1
    for i in range(1,a+1):
        f*=i;
    return f;





#7 recursion
def fact(m):
    if m==1:
        return 1;
    else:
        return(m*fact(m-1));
n=int(input())
f=fact(n)
print("Factorial of a number using recursion=",f);
