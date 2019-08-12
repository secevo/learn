# 00001 Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

---

**Solution:**

最简单的思路自然是暴力扫描两遍，先确定第一个数，再看第二个数和它相加是不是等于目标值，由于题目只允许同一个元素使用一次，所以注意是一个阶梯状循环。显然，这么算的时间复杂度是$O(n^2)$。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
```

能不能只扫描一遍呢？应该说，如果不知道Hash表，还是比较难想到的，只要想到了Hash表，还是很简单的。如果Hash计算时间忽略不计，那么**Hash表是个降低时间复杂度的利器**，尤其是在设计查找的时候。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            else:
                map[nums[i]] = i
```



