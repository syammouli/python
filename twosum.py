################### two sum brute force

a=[2,3,5,6,4,7]
target=11
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            continue
        elif a[i]+a[j]==target:
            
            print(i,j)

#################### two sum using hashing

def two_sum(a,target):
    mpp={}
    for i in range(len(a)):
        num=a[i]
        more_needed=target-num
        if more_needed in mpp:
            return (mpp[more_needed],i)
        mpp[num]=i
        
    return ("not found")
print("twoooooo sum",two_sum(a,target))


################## dutch national flag algorithm to sort 0's 1's and 2's

alg=[0,2,1,0,1,1,1,1,2,2,1,0,1,2,0,1,0]
low=0
mid=0
high=len(alg)-1
for i in range(len(alg)):
    if alg[mid]==0:
        alg[low],alg[mid]=alg[mid],alg[low]
        low+=1
        mid+=1
    elif alg[mid]==1:
        mid+=1
    else:
        alg[mid],alg[high]=alg[high],alg[mid]
        high-=1
        
print ("dutch",alg)

################### majority element that is more than n/2

maj=[2,2,3,4,5,2,2]
maxi={}
n=len(maj)
for num in maj:
    if num not in maxi:
        maxi[num]=1
    else:
        maxi[num]+=1
for key in maxi:
    if maxi[key]>n//2:
        print (key)

################ moores voting algo 
maj = [2,2,3,4,5,2,2]

candidate = 0
count = 0

for num in maj:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

print("Majority element:", candidate)


############### kadanes algo to print max sub array
arr = [-2,1,-3,4,-1,2,1,-5,4]
letmax=float('-inf')
count=0
for num in arr:
    count+=num
    if count>letmax:
        letmax=count

    elif count<0:
        count=0
print("kadaane",letmax)


################## best time to buy & sell stocks

stock=[3,2,6,4,8,5,1]
minimum=stock[0]
profit=0
for i in range(1,len(stock)):
    cost=stock[i]-minimum
    
    profit=max(profit,cost)
    minimum=min(minimum,stock[i])

print(profit)


def rearrange_by_sign(arry):
    nlen=len(arry)
    duparry=[0]*nlen
    pos=0
    neg=1
    for num in arry:
        if num>0:
            duparry[pos]=num
            pos+=2
        else:
            duparry[neg]=num
            neg+=2
    return duparry
    
arry = [3,1,-2,-5,2,-4]

print("rearrangesd",rearrange_by_sign(arry))


####### lets print a brute force solution with random unequal psoitive and negatives

ranarr = [3,1,-2,-5,2,-4,-7,8,9]
def rearrange(ranarr):
    relen=len(ranarr)

    poso=[]
    nego=[]
    i=0
    j=0

    for num in ranarr:
            if num>0:
                    poso.append(num)   
            else:     
                nego.append(num)
    resulting=[]

    while i <len(poso) and j<len(nego):
        resulting.append(poso[i])
        resulting.append(nego[j])
            
        i+=1
        j+=1
    while i < len(poso):
        resulting.append(poso[i])
        i+=1

    while j < len(nego):
        resulting.append(nego[j])
        j+=1
    return resulting
print("unequal rearranging", rearrange(ranarr))


######################### next permutations
# 1️⃣ Find the first decreasing element from the right
# 2️⃣ Find the next larger element on the right side
# 3️⃣ Swap them
# 4️⃣ Reverse the remaining right part


def next_permutation(arr):

    n=len(arr)
    inds=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            inds=i
            break
    if inds==-1:
        arr.reverse()
        return arr
    
    for i in range(n-1,inds,-1):
        if arr[i]>arr[inds]:
            arr[i],arr[inds]=arr[inds],arr[i]
            break

    arr[inds+1:]=reversed(arr[inds+1:])
    return arr

# arr = [1,2,3] 
arr=[2,1,5,4,3,0,0]   

print("Next permutation:", next_permutation(arr))


################## leaders in a array 
leads = [10,22,12,3,0,6]

def findLeads(leads):
    mxEle=leads[-1]
    ele=[]
    ele.append(mxEle)

    for i in range(n-2,-1,-1):
        if leads[i]>mxEle:
            ele.append(leads[i])
            mxEle=leads[i]
        
    return ele
print("leasd",findLeads(leads))

########## longest consequitive sequence
conse=[100,4,200,1,3,2]
longest=0
for num in conse:
  curnt=num
  counts=1
  while curnt+1 in conse:
      curnt+=1
      counts+=1
  longest=max(longest,counts) 
print ("conseeee",longest)


############### matrix , if any element is 0, make the row and column total 0s
def matrix(mat):
    row=set()
    col=set()

    m1=len(mat)
    n1=len(mat[0])

    for i in range(m1):
        for j in range(n1):
            if mat[i][j]==0:
                row.add(i)
                col.add(j)

    for r in row:
        for j in range(n1):
            mat[r][j]=0
    for c in col:
        for j in range(m1):
            mat[j][c] = 0  

    return mat

mat=[
 [1,1,1],
 [1,0,1],
 [1,1,1]
]

print("matrix", matrix(mat))


def rotate(mat90):
    nmat=len(mat90)
    for i in range(nmat):
        for j in range(i+1,nmat):
            mat90[i][j],mat90[j][i]=mat90[j][i],mat90[i][j]

    for i in range(nmat):
        mat90[i].reverse()
    
    return mat90

mat90 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(rotate(mat90))


###############Count Subarray sum Equals K
maxk = [10,22,12,3,0,6,6]
knum=12
addon=0
for i in range(len(maxk)):
    cnt=0
    for j in range(i,len(maxk)):
        cnt+=maxk[j]
        if cnt==knum:
            addon+=1
print("maxk",addon) 


################### ncr pascals traingle, print the element ar given row,col

def nCr(nn,nr):
    if nr>nn:
        return 0
    nr=min(nr,nn-nr)
    resr=1
    for i in range(1,nr+1):
        resr=resr*(nn-i+1)
        resr= resr//i

    return resr
print(nCr(5,3))

############ printing pascal triangle

def print_triangle(tr):
    triangle = []

    for i in range(tr):
        dum = [1] * (i + 1)

        for j in range(1, i):
            dum[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(dum)

    print(triangle)

print_triangle(5)

####### majotity element that is more than n/3
majo = [1,1,1,3,3,2,2,2]
for i in range(len(majo)):
    counting=0
    for j in range(len(majo)):
        if majo[i]==majo[j]:
            counting+=1

    if counting>len(majo)//3:
        print("majority element more than n/3",majo[i])
        break   


#######
def threesome(nums):
    nums.sort()  # Step 1: sort
    resp = []

    for i in range(len(nums)):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right: 
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                resp.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicates for left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicates for right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1   # FIXED

    return resp


# Test
nums = [-1, 0, 1, 2, -1, -4]
print(threesome(nums))


#################################

def fsome(fnums,ftarget):
    fnums.sort()
    fresp=[]
    for i in range(len(fnums)):
        if i >0 and fnums[i]==fnums[i-1]:
            continue
        for j in range(len(fnums)):
            if j>i+1 and fnums[j]==fnums[j-1]:
                continue

            fleft=j+1
            fright=len(fnums)-1
            while fleft<fright:
                if ftarget==fnums[i]+fnums[j]+fnums[fleft]+fnums[fright]:
                    fresp.append([fnums[i],fnums[j],fnums[fleft],fnums[fright]])
                    fleft+=1
                    fright-=1

                    while fleft< fright and fnums[fleft]==fnums[fleft-1]:
                        fleft+=1
                    while fleft<fright and fnums[fright]==fnums[fright+1]:
                        fright-=1
                elif fnums[i]+fnums[j]+fnums[fleft]+fnums[fright]<ftarget:
                    fleft+=1
                else:
                    fright -=1
    return fresp




fnums = [1, 0, -1, 0, -2, 2]
ftarget = 0

print("foursome",fsome(fnums,ftarget))

xnm=[4,2,2,6,4]
def xor(xnm):
    for i in range(len(xnm)):
        xnum=0
        for j in range(len(xnm)):
            xnum=xnum^xnm[j]
            if xnum==6:
                xnum+=1
    return xnm
print (xor(xnm))

################## merge intervals
def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    merged=[]
    for interval in intervals:
        if not merged or interval[0]>merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1]=max(merged[-1][1],interval[1])

    return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))


###################### merge two sort arrays using gap method(shell sort)
def gap_num(lens):
    if lens<=1:
        return 0
    return (lens//2)+(lens%2)

def mergeGap(arr1,arr2):
    lenar1=len(arr1)
    lenar2=len(arr2)
    gap=gap_num(lenar1+lenar2)

    while gap>0:
        i=0
        j=gap
        while j < (lenar1+lenar2):
            if i< lenar1 and j < lenar1:
                if arr1[i]>arr1[j]:
                    arr1[i],arr1[j]=arr1[j],arr1[i]
            elif i< lenar1 and j >=lenar1:
                if arr1[i]>arr2[j-lenar1]:
                    arr1[i],arr2[j-lenar1]=arr2[j-lenar1],arr1[i]
            else:
                if arr2[i-lenar1]>arr2[j-lenar1]:
                    arr2[i-lenar1],arr2[j-lenar1]=arr2[j-lenar1],arr2[i-lenar1]

            i+=1
            j+=1
        gap=gap_num(gap)

            


arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]

mergeGap(arr1, arr2)

print("gap method",arr1)
print(arr2)


############ find the missing and repeating numbers in an array
sumar=[1, 2, 2, 4]
nmis=len(sumar)
def find_missing_repeating(sumar):
    diff=(nmis*(nmis+1))//2
    sq_diff=((nmis*(nmis+1)*(2*nmis+1)))//6

    act_diff=sum(sumar)
    act_sq_diff=sum(x*x for x in sumar)

    normal=act_diff - diff
    sq_normal=act_sq_diff-sq_diff

    sumxy=sq_normal//normal

    repeating = (normal+sumxy)//2
    missing= repeating-normal
    return repeating, missing

print("repeating,missing",find_missing_repeating(sumar))


############### count inversions in an array
def merged(merarr, merlow, mermid, merhigh):
    tempo = []
    left = merlow
    right = mermid + 1
    count = 0

    # Merge step
    while left <= mermid and right <= merhigh:

        if merarr[left] <= merarr[right]:
            tempo.append(merarr[left])
            left += 1
        else:
            tempo.append(merarr[right])

            # Count inversions
            count += (mermid - left + 1)

            right += 1

    # Remaining left elements
    while left <= mermid:
        tempo.append(merarr[left])
        left += 1

    # Remaining right elements
    while right <= merhigh:
        tempo.append(merarr[right])
        right += 1

    # Copy back to original array
    for i in range(merlow, merhigh + 1):
        merarr[i] = tempo[i - merlow]

    return count


def merge_sort(merarr, merlow, merhigh):
    counts = 0

    if merlow < merhigh:
        # FIXED mid
        mermid = (merlow + merhigh) // 2

        counts += merge_sort(merarr, merlow, mermid)
        counts += merge_sort(merarr, mermid + 1, merhigh)
        counts += merged(merarr, merlow, mermid, merhigh)

    return counts


# Example
merarr = [5, 3, 2, 4, 1]
print(merge_sort(merarr, 0, len(merarr) - 1))


################# reverse pairs
rev=[40,25,119,12,9,6,2]
revvcnt=0
for i in range (len(rev)):
    for j in range(i+1,len(rev)):
        if rev[i]>rev[j]*2:
            revvcnt+=1

print ("prev num is > twice of next",revvcnt)

################## optimal approach

def countrev(rev,low, mid,high):
    count=0
    right=mid+1
    for i in range(low,mid+1):
        while right<=high and rev[i]>2*rev[right]:
            right+=1

        count+=(right-(mid+1))

    return count

def merging(rev,low,mid,high):
    temped=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if rev[left]<=rev[right]:
            temped.append(rev[left])
            left+=1
        else:
            temped.append(rev[right])
            right+=1

    while left<=mid:
        temped.append(rev[left])
        left+=1

    while right<=high:
        temped.append(rev[right])
        right+=1

    for i in range(low,high+1):
        rev[i]=temped[i-low]

           
def merge_rev(rev,low,high):
    if low >= high:
        return 0
    counting=0
        
    mid=(low+high)//2
    counting+=merge_rev(rev,low,mid)
    counting+=merge_rev(rev,mid+1,high)

    counting+=countrev(rev,low,mid,high)
    merging(rev,low,mid,high)
    return counting
print("printing num>twice using mergesort",merge_rev(rev,0,len(rev)-1))


########### max product subarray

numspro = [2, 3, -2, 4]
def max_prod(numspro):
    miniprod=numspro[0]
    maxiprod=numspro[0]
    resultss=numspro[0]
    

    for i in range(1,len(numspro)):
        nn=numspro[i]
        if nn<0:
            miniprod,maxiprod=maxiprod,miniprod

        maxiprod=max(nn,maxiprod*nn)
        miniprod-min(nn,miniprod*nn)

        resultss=max(maxiprod,resultss)

    return resultss

print("maxi sub array of products",max_prod(numspro))