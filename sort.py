print("selection sort")

arr=[13,46,24,52,20,9]
leng=len(arr)

for i in range(leng-1):
    mini=i
    for j in range(i+1,leng):
        if arr[j]<arr[mini]:
            mini=j

    arr[i],arr[mini]=arr[mini],arr[i]
print(arr)

print("bubblesort")
arr1=[13,46,24,52,20,9]
lengt=len(arr)

for i in range(lengt-1):
    for j in range(lengt-i-1):
        if arr1[j]>arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
print (arr1)


################# insertion sort

a=[13,17,7,10,12,22]

n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
print(a)


############### merge sort

def merge_sort(marr):
    if len(marr)>1:
        mid=len(marr)//2
        left=marr[:mid]
        right=marr[mid:]
        i=0
        j=0
        k=0
        merge_sort(left)
        merge_sort(right)
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                marr[k]=left[i]
                i+=1
            else:
                marr[k]=right[j]
                j+=1
            k+=1

        while i< len(left):
            marr[k]=left[i]
            i+=1
            k+=1
        while j< len(right):
            marr[k]=right[j]
            j+=1
            k+=1

marr=[2,1,4,5,2,3,4,7]
merge_sort(marr)
print(marr)

############ quick sort

def quick_sort(qarr, low, high):

    if low < high:

        pivot_index = partition(qarr, low, high)

        quick_sort(qarr, low, pivot_index - 1)

        quick_sort(qarr, pivot_index + 1, high)


def partition(qarr, low, high):

    pivot = qarr[low]   # first element as pivot

    i = low + 1
    j = high

    while True:

        while i <= j and qarr[i] <= pivot:
            i += 1

        while i <= j and qarr[j] >= pivot:
            j -= 1

        if i > j:
            break

        qarr[i], qarr[j] = qarr[j], qarr[i]

    qarr[low], qarr[j] = qarr[j], qarr[low]

    return j


qarr = [2,1,4,5,2,3,4,7,92,54]

quick_sort(qarr, 0, len(qarr)-1)

print(qarr)


################# remove duplicates from the array

dup=[0, 0, 3, 3, 5, 6]
def duplicates(dup):
    i=0
    for j in range(i+1,len(dup)):
        if dup[i]!=dup[j]:
            dup[i+1]=dup[j]
            i+=1
        
    print(dup[:i+1])

duplicates(dup)

###### left rotate the array

rot=[8,7,6,5]
def rotate(rot):
    temp=rot[0]
    for i in range(1,len(rot)):
        rot[i-1]=rot[i]
    rot[len(rot)-1]=temp
    print (rot)

rotate(rot)
print("left rotate")
########### move zeroes to the right

def zeroToright(xer):
    pos=0
    for i in range(len(xer)):
        if xer[i]!=0:
            xer[pos],xer[i]=xer[i],xer[pos]
            pos += 1   # missing line

    print(xer)

zeroToright([1,0,2,1,0,0,0])



########union of arrays
arr1 = [1, 2, 3, 4]      
arr2 = [3, 4, 5, 6]    
com=[]
for x in arr1+arr2:
    if x not in com:
        com.append(x)

print("com",com)
    

############### intersection of sorted arrays
a = [1, 2, 2, 3, 4]   # first sorted array
b = [2, 2, 4, 6]      # second sorted array

def intersection(a, b):
    n1 = len(a)       # length of first array
    n2 = len(b)       # length of second array

    i, j = 0, 0       # pointers for arrays
    result = []       # list to store intersection

    # loop until one array finishes
    while i < n1 and j < n2:

        if a[i] < b[j]:      # if element in a is smaller
            i += 1           # move pointer i

        elif a[i] > b[j]:    # if element in b is smaller
            j += 1           # move pointer j

        else:                # if both elements are equal

            # add element only if result is empty or last element is different
            if not result or result[-1] != a[i]:
                result.append(a[i])

            i += 1           # move both pointers
            j += 1

    print(result)            # print intersection


intersection(a, b)


################ find the missing element in sorted array
sot=[1,2,3,5]
tot=0
for num in sot:
    print("num")
    tot+=num
    print(tot)
sums=len(sot)+1*(len(sot)+2)/2
print("missed",tot-sums)
le=len(sot)+1
hash_set=set(sot)
for i in range (1,le):
    if i not in hash_set:
        print(i)

############# max consecutive ones in a array

cons=[1,1,0,1,1,1,0,1,1,1,1,0,0,1]
maxi=0
counts=0
for num in cons:
    if num==1:
        counts+=1
        maxi=max(counts,maxi)
    else:
        counts=0
print(maxi)

################## find the number that appears once, in a array of twices

tei=[1,1,2,2,3,4,4,5,5]

for i in range(len(tei)):
    numss=tei[i]
    count=0
    for j in range(len(tei)):
        if numss==tei[j]:
            count+=1
    if count==1:
        print("single",numss)


###################### using xor

rref=0
for num in tei:
    rref^=num
print(rref)

#############print longest subarrays
lonarr = [1, 2, 1, 1, 1, 2, 3]
k=3
i=0
max_len=0
counts=0
starts=-1
ends=-1
for j in range (len(lonarr)):
    counts+=lonarr[j]
    while counts>k and i <=j:
        counts-=lonarr[j]
        i+=1
    if counts==k:
        if j-i+1>max_len:
            max_len=j-i+1
            starts=i
            ends=j
    if starts!=-1:
            print("Longest subarray:", arr[starts:ends+1])   # print the subarray
            print("Length:", max_len)                      # print the length of the subarray
    else:
            print("No subarray found")   