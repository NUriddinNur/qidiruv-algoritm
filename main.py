---------------------------
# Linear searching      
---------------------------

mylist1 = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]


def searching(mas, n):
    for i in range(len(mas)):
        if mas[i] == n:
            return i
    return None

print(searching(mylist1, 10))

----------------------------
Binary search
----------------------------

mylist1 = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]

def binary2(arr, p):
    l = 0
    h = len(arr) - 1
    if l > h:
        return False
    else:
        for i in range(len(arr)):
            m = (l + h) // 2
            if arr[m] == p:
                return m
            elif arr[m] > p:
                h = m - 1
            elif arr[m] < p:
                l = m + 1

print(binary2(mylist1, 99))


mylist1 = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]     #binary search  while blan
mylist1 = ['a','b','c','d','e','f','g','h','i','j']

def binary_search(list, n):
    l = 0
    h = len(list) - 1
    while l <= h:
        m = (l + h) // 2
        if list[m] == n:
            return m
        if list[m] > n:
            h = m - 1
        if list[m] < n:
            l = m + 1

    return None

print(binary_search(mylist1, 'j'))

