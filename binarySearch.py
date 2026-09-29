import math
num=[2,3,4,5,6,7,8,9]
def binary(num,target):
    low= 0
    high=len(num)-1
    while low<=high:
        mid=(low+high)//2
        
        if target==num[mid]:
            return mid
        elif target>num[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
print("binary search",binary(num,6))


    
########## same binary using recursion
def binary_rec(num,low,high,target):
        if low>high:
            return -1
    
        mid=(low+high)//2
        if target==num[mid]:
            return mid
        elif target>num[mid]:
            return binary_rec(num,mid+1,high,target)
        else:
            return binary_rec(num,low,mid-1,target)
        
print("binary search recursion",binary_rec(num,0,len(num),7))

########implement upperbound and lower bound
num1=[2,3,4,5,7,8,9]

def lower_bound(num1,target):
    low=0
    high=len(num1)-1
    ans=len(num1)
    while low<=high:
        mid=(low+high)//2
        
        if num1[mid]>=target: ########if = is removed, it returns lower bound
         ans=mid
         high=mid-1

        else:
            low=mid+1
    return ans

print("lower bound", lower_bound(num1,10))


########### search element in a rotated array

def search_rotated(rota,target):
    low,high=0,len(rota)-1
    while low<=high:
        mid=(low+high)//2
        if rota[mid]==target:
            return mid
        if rota[low]<=rota[mid]:
            if rota[low]<=target<rota[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if rota[mid]<target<=rota[high]:
                low=mid+1
            else:
                high=mid-1

    return -1
# rota = [4, 5, 6, 7, 0, 1, 2]
rota=[3,3,3,3,1,2,3,4]
target = 3


def search_rotated(rota,target):
    low,high=0,len(rota)-1
    while low<=high:
        mid=(low+high)//2
        if rota[mid]==target:
            return mid
        if rota[low]==rota[mid]==rota[high]:
            low+=1
            high-=1
            continue
        if rota[low]<=rota[high]:
            if rota[low]<=target<rota[mid]:
                high=mid-1
            else:
                low=mid+1

        else:
            if rota[mid]<target<=rota[high]:
                low=mid+1
            else:
                high=mid-1

    return -1
print ("search in rotated element",search_rotated(rota,target))

############ minimum in a rotated array

def minimum(mini):
    low,high=0,len(mini)-1
    ans=float('inf')
    while low<=high:
       
        if mini[low]<=mini[high]:
            ans=min(ans,mini[low])
            break
        mid=(low+high)//2
        if mini[low]<=mini[mid]:
            ans=min(ans,mini[low])
            low=mid+1
        else:
            ans=min(ans,mini[mid])
            high=mid-1
    return ans
   
mini = [4, 5, 6, 7,  1, 2]

print ("minimum in rotated element",minimum(mini))

########## find how many times array is rotated [index of lowest element will give you the answer]
def times_rotated(mini):
    low,high=0,len(mini)-1
    ans=float('inf')
    ind=-1
    while low<=high:
        mid=(low+high)//2
        if mini[low]<=mini[high]:
            ans=min(ans,mini[low])
            ind=low
            break
        elif mini[low]<=mini[mid]:
            ans=min(ans,mini[low])
            ind=low
            low=mid+1
        else:
            ans=min(ans,mini[mid])
            high=mid-1
            ind=mid
    return ind
print("times rotated",times_rotated(mini))


############## single element

def single_element(singles):
    low,high=0,len(singles)-1
    while low<high:
        mid=(low+high)//2
        if mid%2==1:
            mid-=1
        if singles[mid]==singles[mid+1]:
            low=mid+2
        else:
            high=mid
    return singles[low]

singles = [1,1,2,2,3,3,4,4,5]
print("Single element:", single_element(singles))

########## find peak in a array

def find_peak(peak):
    n=len(peak)
    if peak[0]>peak[1]:
        return peak[0]
    if peak[n-1] > peak[n-2]:
        return peak[n-1]
    low=1
    high=n-2
    while low<high:
        mid=(low+high)//2
        if peak[mid] > peak[mid-1] and peak[mid] > peak[mid+1]:
            return peak[mid]
        elif peak[mid]<peak[mid+1]:
            low=mid+1

        else:
            high=mid-1

print("finding peak", find_peak([1,2,3,4,5,4,3]))


############# closest sqrt of a number
def sqrt(sqrs):
    low,high=0,sqrs
    ans=0
    while low<high:
        mid=(low+high)//2
        if (mid*mid)<=sqrs:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

sqrs=28
print("sqrt element:", sqrt(38))


###################### finding the nth root of a number

def findingN(n):
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        print(mid*mid*mid,"chefck")
        if (mid*mid*mid)==n:
            return mid
        elif (mid*mid*mid)>n:
            high=mid-1
        else:
            low=mid+1

    return -1

print("finding n:", findingN(27))

###### KOKO eating banans

def koko(heaps,h):
    low=1
    high=max(heaps)
    while low<=high:
        mid=(low+high)//2
        hours_taken=0

        for heap in heaps:
            hours_taken+=math.ceil(heap/mid)
        if hours_taken <= h:
            high=mid-1
        else:            
            low=mid+1
    return low

print("koko",koko([3,6,7,11],8))


########### BS-13. Minimum days to make M bouquets | Binary Search
#m=number of bouquets
#k=adjacent flowers
# def minDays(bloomDay,m,k):
#     n=len(bloomDay)
#     if m*k>len(bloomDay):
#         return -1
#     def canMake(day):
#         flowers=0
#         bouquets=0
#         for b in bloomDay:
#             if b<=day:
#                 flowers+=1
#                 if flowers==k:
#                     bouquets+=1
#                     flowers=0
#                 else:
#                     flowers=0

#         return bouquets>=m

#     low=min(bloomDay)
#     high=max(bloomDay)
#     ans=-1
#     while low<=high:
#         mid=(low+high)//2
#         if canMake(mid):
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans


def minDays(bloomDay,m,k):
    low=min(bloomDay)
    high=max(bloomDay)
    if (m*k)>len(bloomDay):
        return -1
    def canBloom(day):
        flowers=0
        bouquets=0
        for b in bloomDay:
            if b<=day:
                flowers+=1
                if flowers==k:
                    bouquets+=1
                    flowers=0
                else:
                    flowers=0
        return bouquets>=m
            
    while low<=high:
        mid=(low+high)//2
        ans=0
        if canBloom(mid):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

bloomDay = [1,10,3,10,2]
m = 3
k = 1

print("bouquetssssssssssss",minDays(bloomDay, m, k))


# BS-14. Find the Smallest Divisor Given a Threshold | Binary Search

def smallestDivisor(arr,threshold):
    
    def counts(numb):
        total=0
        for num in arr:
            total+=math.ceil(num/numb)
            
        return total
    
    low=1
    high=max(arr)
    ans=high
    while low<=high:
        mid=(low+high)//2
        if counts(mid)<=threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


nums = [1,2,5,9]
threshold = 6

print("smalest Divisor",smallestDivisor(nums, threshold))

# BS-15. Capacity to Ship Packages within D Days

def shipWithinDays(weights,days):
    def daysCount(capacity):
        days_needed=1
        current_weight=0
        for w in weights:
            if current_weight+w>capacity:
                days_needed+=1
                current_weight=w
            else:
                current_weight+=w
        return days_needed

    low=max(weights)
    high=sum(weights)
    
    while low<=high:
        mid=(low+high)//2
        if daysCount(mid)<=days:            
            high=mid-1
        else:
            low=mid+1
    return low

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print("capacity of ship",shipWithinDays(weights, days))



# BS-16. Kth Missing Positive Number | Maths + Binary Search

def findKthPositive(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    # answer = k + number of elements before low
    return low + k

arr = [2,3,4,7,11]
k = 5
print("k + elements",findKthPositive(arr,k))

# BS-17. Aggressive Cows | Binary Search Hard
def aggressiveCows(cows,k):
    cows.sort()
    low=cows[0]
    high=cows[-1]-cows[0]
    def canWePlace(lengths):
        lastCow=cows[0]
        minimLength=1
        for i in range(1,len(cows)):
            if cows[i]-lastCow>=lengths:
                minimLength+=1
                lastCow=cows[i]
            if minimLength>=k:
                return True
        return False


    while low<=high:
        mid=(low+high)//2
        if canWePlace(mid):
            low=mid+1
        else:
            high=mid-1
    return high

cows = [1,2,4,8,9]
k = 3

print("aggressive cows", aggressiveCows(cows,k))


# BS-18. Allocate Books or Book Allocation | Hard Binary Search

def bookAllocation(arr,m):
    if m>len(arr):
        return -1
    
    def checkAllocation(maxpages):
        pageinbook=0
        students=1
        for i in range(len(arr)):
            if pageinbook+arr[i]>maxpages:
                students+=1
            if students>m:
                return False
            else:
                pageinbook+=arr[i]

        return True

    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        if checkAllocation(mid):
            high=mid-1
        else:
            low=mid+1
    return low
arr = [25, 46, 28, 49,24]
m = 4
print("bookAllocation",bookAllocation(arr,m))

#painters partition
def paintersPartition(arr, k):
    if k > len(arr):
        return -1

    low = max(arr)
    high = sum(arr)

    def checkAllocation(maxValue):
        painter = 1
        count = 0

        for i in range(len(arr)):

            # If adding current board exceeds maxValue
            if count + arr[i] > maxValue:
                painter += 1
                count = arr[i]   # assign new painter

                if painter > k:
                    return False
            else:
                count += arr[i]  # continue with same painter

        return True

    while low <= high:
        mid = (low + high) // 2

        if checkAllocation(mid):
            high = mid - 1
        else:
            low = mid + 1

    return low


# Input
arr = [10, 20, 30, 40]
k = 2

print("painters partition:", paintersPartition(arr, k))

########## gas stations

def gasStations(arr,k):
    maximm=0
    for i in range(len(arr)):
        maximm=max(maximm,arr[i]-arr[i-1])
    low=0
    high=maximm

    def canPlace(dist):
        count=0
        for i in range(1,len(arr)):
            gap=arr[i]-arr[i-1]
            count+=int(gap/dist)
        return count
    while high-low>1e-6:
        mid=(low+high)/2
        if canPlace(mid)>k:
            low=mid
        else:
            high=mid
    return high

arr = [1, 2, 3, 4, 5]
k = 4
print("gas stations",gasStations(arr,k))


# BS-21. Median of two Sorted Arrays of Different Sizes | Binary Search Approach With Intuition

def findMedian(A, B):
    n1 = len(A)
    n2 = len(B)

    # Ensure A is smaller
    if n1 > n2:
        return findMedian(B, A)

    total = n1 + n2
    low, high = 0, n1

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (total + 1) // 2 - cut1

        left1 = float('-inf') if cut1 == 0 else A[cut1 - 1]
        right1 = float('inf') if cut1 == n1 else A[cut1]

        left2 = float('-inf') if cut2 == 0 else B[cut2 - 1]
        right2 = float('inf') if cut2 == n2 else B[cut2]

        # Correct condition (use <= for safety)
        if left1 <= right2 and left2 <= right1:

            if total % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1


print("med using binary",findMedian([1,2],[2,3,4]))

############### finding kth element using binary
def kthElement(A, B, k):
    n1 = len(A)
    n2 = len(B)

    # Always binary search on smaller array
    if n1 > n2:
        return kthElement(B, A, k)

    # Define search range for cut1
    low = max(0, k - n2)   # minimum elements we must take from A
    high = min(k, n1)      # maximum elements we can take from A

    while low <= high:
        cut1 = (low + high) // 2   # elements taken from A
        cut2 = k - cut1            # elements taken from B

        # Example:
        # k = 5, cut1 = 2 → cut2 = 3
        # So total left elements = 5

        # Left and right values from A
        left1 = float('-inf') if cut1 == 0 else A[cut1 - 1]
        right1 = float('inf') if cut1 == n1 else A[cut1]

        # Left and right values from B
        left2 = float('-inf') if cut2 == 0 else B[cut2 - 1]
        right2 = float('inf') if cut2 == n2 else B[cut2]

        # Check correct partition
        if left1 <= right2 and left2 <= right1:
            # We found valid split
            return max(left1, left2)

        elif left1 > right2:
            # Too many elements taken from A → move left
            high = cut1 - 1
        else:
            # Too few elements from A → move right
            low = cut1 + 1


A = [2,3,6,7,9]
B = [1,4,8,10]
k = 5
print ("print k element", kthElement(A,B,k))


############## find max ones

def findMax1(matrix):
    row=len(matrix)
    col=len(matrix[0])
    maxones=0
    index=-1
    def findIndex(mat):
        low=0
        high=col-1
        ans=col
        while low<=high:
            mid=(low+high)//2
            if mat[mid]==1:
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans

    for i in range(row):
        first=findIndex(matrix[i])
        totalOnes=col-first
        if totalOnes>maxones:
            index=i
            maxones=totalOnes
    return maxones
matrix = [
    [0,0,1,1],  
    [0,1,1,1], 
    [0,0,0,1],   
]

print("print index of highest onnes",findMax1(matrix))

########### search element in a 2d array

def searchin2D(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    low=0
    high=n*m-1
    while low<=high:
        mid=(low+high)//2
        row=mid//m
        col=mid%m
        value=matrix[row][col]
        if value==target:
            return True
        if value<mid:
            high=mid-1
        else:
            low=mid+1
    return False
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 12

print("search in 2d:",searchin2D(matrix,target))
############## search in 2d array part 2 where only either cols or rows are sorted, we check from 
#top right index here

def searchin2dpart2(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    row= 0
    col=m-1
    while row<n and col>=0:
        currrent=matrix[row][col]
        if target==currrent:
            return True
        elif currrent>target:
            col-=1
        else:
            row+=1
    return False

matrix2 = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10,13,14,17]
]
target = 5

print("search in 2d part2",searchin2dpart2(matrix2,3))


################ finding peak in a 2d array
def peakMatrix(matrixPeak):
    n=len(matrixPeak)
    m=len(matrixPeak[0])

    low=0
    high=m-1
    while low<=high:
        mid=(low+high)//2
        max_element=0
        for i in range(n):
            if matrixPeak[i][mid]>matrixPeak[max_element][mid]:
                max_element=i
        current=matrixPeak[max_element][mid]
        left=matrixPeak[max_element][mid-1] if mid-1>0 else -1
        right=matrixPeak[max_element][mid+1] if mid+1<m else -1

        if current>left and current>right:
            return [max_element,mid]
        elif left>current:
            high=mid-1
        else:
            low=mid+1
    return [-1,-1]

matrixPeak = [
    [10, 20, 15],
    [21, 30, 14],
    [7,  16, 32]
]
print("peak in matrix", peakMatrix(matrixPeak))


####BS-27. Median in a Row Wise Sorted Matrix
def findMedianin(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Step 1: find min and max
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    # Required position of median
    req = (n * m) // 2

    # Function to count elements <= x
    def countLessEqual(x):
        count = 0
        for row in matrix:
            # Binary search in each row
            low_r, high_r = 0, m - 1

            while low_r <= high_r:
                mid = (low_r + high_r) // 2

                if row[mid] <= x:
                    low_r = mid + 1
                else:
                    high_r = mid - 1

            # low_r gives count of elements <= x
            count += low_r

        return count

    # Step 2: binary search on answer
    while low <= high:
        mid = (low + high) // 2

        if countLessEqual(mid) <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low



matrixo = [
    [1,3,5],
    [2,6,9],
    [3,6,9]
]
print("find",findMedianin(matrixo))