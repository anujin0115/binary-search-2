# You can remove 'pass' if you written code in the function
# Exercise 1
def find_closest(data, target):
    low=0
    high=len(data)-1

    if data[low]>target:
        return data[low]
    if data[high]<target:
        return data[high]

    while low<=high:
        mid = (low + high ) //2
        if data[mid] == target:
            return data[mid]
        elif data[ mid ] < target:

            if mid + 1 < len(data) and data[mid + 1] > target:
                if abs(data[mid] - target) < abs(data[mid+1] - target):
                    return data[ mid ]
                elif abs(data[mid] - target) == abs(data[mid+1] - target):
                    return data[mid]
                else:
                    return data [ mid+1 ]
            low = mid + 1
        else:
            if  mid-1>=0 and data[ mid-1 ] < target :
                if abs(data[mid] - target) < abs(data[mid-1] - target):
                    return data[ mid ]
                elif abs(data[mid] - target) == abs(data[mid+1] - target):
                    return data[mid-1]
                else:
                    return data [ mid-1 ]
            high=mid-1

# Exercise 2
def integer_sqrt(n):
    # Write your code here
    pass
def integer_sqrt(n):
    low = 0
    high = n
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid <= n:
            answer = mid      
            low = mid + 1
        else:
            high = mid - 1

    return answer




