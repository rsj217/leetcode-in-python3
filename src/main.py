
import functools



def compare(a, b):
    ab = a + b
    ba = b + a
    if ab < ba:
        return 1
    return -1

nums = [10,2,9,39,17]
nums_list = [str(i) for i in nums]
nums_list.sort(key=functools.cmp_to_key(compare))

print(nums_list)