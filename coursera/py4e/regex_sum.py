import re

handle = open('regex_sum_350301.txt')

nums = list()
for line in handle:
    r = re.findall("[0-9]+", line)
    if len(r) == 0:
        continue
    nums = nums + [int(s) for s in r]

print(sum(nums))
