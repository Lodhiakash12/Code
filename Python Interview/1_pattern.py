
#Rectangle
n=int(input("ENter N:"))


for r in range(1,n+1):
    for c in range(n):
        print("*", end=" ")
    print()



#1.Right Angle Triangle


for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

* 
* * 
* * * 
* * * * 
* * * * * 

#2.Inverted Right Angle


for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#1.Number Angle Triangle


for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()


1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 


#2.Number Col

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5




    




