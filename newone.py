#find the higest common factor or greatest common division
a=int(input("enter a number"))
b=int(input("enter a number"))
while b!=0:
    a,b=b,a%b
print("HCF/GCD=",a)
#to find LCM OF two number
n=int(input("enter a number"))
num=int(input("enter a number"))
x=n
y=num
while y!=0:
    n,num=num,num%n
GCD=a
LCM=(x*y)//GCD
print("LCM=",LCM)
            


