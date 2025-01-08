def average(array):
    nums = set(array)
    return sum(nums)/len(nums)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)