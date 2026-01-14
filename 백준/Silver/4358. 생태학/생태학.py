import sys
from collections import defaultdict

input = sys.stdin.read

trees = input().splitlines()
_dict = defaultdict(lambda: 0)
sum = 0

for tree in trees:
    _dict[tree] += 1
    sum += 1

for k in sorted(_dict.keys()):
    ratio = (_dict[k] / sum) * 100
    print(f"{k} {ratio:.4f}")