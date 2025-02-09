import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"4th element at {arr} is {arr[3]}")

print(f"4-8th index elements are {arr[3:8]}")

print(arr.reshape(5,2))
print(arr.reshape(2,5))

for i in arr:
    print(i)

arr2 = np.array([1, 2, 3,])
arr3 = np.array([4, 5, 6,])
joint = np.concatenate(arr2, arr3)

print(arr.find(5))
