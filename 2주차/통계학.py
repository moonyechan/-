import sys

input = sys.stdin.read

lines = input().split()
n = int(lines[0]) 
nums = list(map(int, lines[1:])) 

avg = round(sum(nums) / n)

nums.sort()
med = nums[n // 2]

counts = {}  
for num in nums:
    if num not in counts:  
        counts[num] = 1
    else:  
        counts[num] += 1

max_cnt = 0
for count in counts.values():
    if count > max_cnt:
        max_cnt = count

modes = []
for num, count in counts.items():
    if count == max_cnt:
        modes.append(num)

modes.sort()  
mode = modes[1] if len(modes) > 1 else modes[0]  

rng = nums[-1] - nums[0]

print(avg)
print(med)
print(mode)
print(rng)
