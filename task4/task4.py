import sys


with open(sys.argv[1]) as roster:
    nums = roster.read().splitlines()

nums = [int(item) for item in nums]

nums = sorted(nums)
median = nums[len(nums)//2]
ShortCut = sum(abs(n - median) for n in nums)

print(ShortCut)


