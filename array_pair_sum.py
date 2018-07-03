# def pairSum2(arr, k):
#     if len(arr)<2:
#         return
#     seen=set()
#     output=set()
#     for num in arr:
#         target=k-num
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add( (min(num, target), max(num, target)) )

def pairSum1(arr, k):
    if len(arr)<2:
        return
    arr.sort()
    left, right = (0, len(arr)-1)
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==k:
            print arr[left], arr[right]
            left+=1 #or right-=1
        elif currentSum<k:
            left+=1
        else:
            right-=1
            
arr = [1, 3, 2, 1, 4]
k = 4

pairSum1(arr, k)
