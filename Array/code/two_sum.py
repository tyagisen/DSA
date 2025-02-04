# Two sum to find target element

def twoSum(arr, target):
    nmap_store = {}
    for i, num in enumerate(arr):
        val = target-num
        if val in nmap_store:
            return [nmap_store[val], i]
        nmap_store[num]=i

arr = [1,5,7,14]
target = 12

print(twoSum(arr, target))