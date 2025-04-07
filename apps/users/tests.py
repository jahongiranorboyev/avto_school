import requests


# print(requests.get(url="http://1516-90-156-198-203.ngrok-free.app/api/v1/lessons/").json())
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
sort1 = quick_sort([5, 3, 8, 4, 2])

print(sort1)
