from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        sorted = True
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                sorted = False
        if sorted:
            return nums
    return nums

def selectionSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[min_idx] > nums[j]:
                min_idx = j
        tmp = nums[i]
        nums[i] = nums[min_idx]
        nums[min_idx] = tmp
    return nums


def insertionSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        pre = i - 1
        tmp = nums[i]
        while pre >= 0 and tmp < nums[pre]:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = tmp
    return nums

def shellSort(nums: List[int]) -> List[int]:
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            pre = i
            tmp = nums[i]
            while pre >= gap and nums[pre-gap] > tmp:
                nums[pre] = nums[pre-gap]
                pre -= gap
            nums[pre] = tmp
        gap = gap // 2
    return nums


def mergeSort(nums: List[int], s: int, e: int) -> List[int]:

    def merge(nums, s, m, e):
        
        '''
        :type nums: List[int]
        :type s: int, start index
        :type m: int, middle index
        :type e: int, end index
        '''
        nums_l = []
        nums_r = []
        for i in nums[s:m]:
            nums_l.append(i)
        for i in nums[m:e+1]:
            nums_r.append(i)
        import sys
        nums_l.append(sys.maxsize)
        nums_r.append(sys.maxsize)
        
        i=j=0
        for k in range(s, e):
            if nums_l[i] < nums_r[j]:
                nums[k] = nums_l[i]
                i += 1
            else:
                nums[k] = nums_r[j]
                j += 1

    if s < e:
        m = (s + e) // 2
        mergeSort(nums, s, m)
        mergeSort(nums, m, e)
        merge(nums, s, m, e)







if __name__ == '__main__':
    import random
    # nums = [i for i in range(10)]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    # nums = bubbleSort(nums)
    # nums = selectionSort(nums)
    # nums = insertionSort(nums)
    # nums = shellSort(nums)
    mergeSort(nums, 0, len(nums))
    print(nums)
