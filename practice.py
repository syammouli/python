#practice

# Input :
A = [1, 2, 3, 4, 5]
# Output : [48]
#          [20, 28] 
#          [8, 12, 16] 
#          [3, 5, 7, 9] 
#          [1, 2, 3, 4, 5] 

def printTriangle(A):
    n=len(A)
    if n<1:
        return
    temp=[0]*(n-1)
    for i in range(0, n-1):
        x=A[i]+A[i+1]
        temp[i]=x
    printTriangle(temp)
    print(A)

printTriangle(A)


###### finding min max
def minMax(arr,n):
    if n==1:
        return arr[0],arr[0]
    mini,maxi=minMax(arr,n-1)
    if arr[n-1]<mini:
        mini=arr[n-1]
    if arr[n-1]>maxi:
        maxi=arr[n-1]
    return mini,maxi
arr = [3, 5, 1, 8, 2, 9]
mn,mx=minMax(arr,len(arr))
print(mn,mx)

# uppercase in word

def upper(word):
    for wor in word:
        if wor.isupper():
            return wor
    return "not found"

print(upper("hello orld"))

#### rev a string

stri="hello"
print(stri[::-1])

#print 1 to n using recursion

def printNum(n):
    if n==0:
        return
    printNum(n-1)
    print(n)

printNum(10)

#print length
geek="GEEKSFORGEEKS"
def geeko(geek):
    if geek=="":
        return 0
    return 1+geeko(geek[1:])

print(geeko(geek))