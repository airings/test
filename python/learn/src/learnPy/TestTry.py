'''
Created on Apr 27, 2016

@author: airings
'''
nums = [1,2,3,1,1,1]

for num in set(nums):
    if nums.count(num) > len(nums)/2:
        print num