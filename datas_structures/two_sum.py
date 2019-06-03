#### TOO SLOW FOR LEETCODE ####

#def two_sum(nums, target):
#    
#    for i in range(len(nums) - 1):
#        j = i + 1;
#        while j < len(nums):
#            cur = nums[i] + nums[j];
#            while target % 2 != 0 and ((nums[i] % 2 == 0 and nums[j] % 2 == 0)\
#                    or (nums[i] % 2 != 0 and nums[j] % 2 != 0)):
#                j += 1;
#            if cur == target:
#                result = [i, j];
#                return result;
#            j += 1;

##_____________________________________________________________##

def two_sum(nums, target):

    for i in range(len(nums)):
        temp = target - nums[i];
        if temp in nums and nums.index(temp) != i:
            if nums.index(temp) < i:
                result = [nums.index(temp), i];
            else:
                result = [i, nums.index(temp)];
            return result;

nums = [2,7,11,13,24]
target = 15;
print(two_sum(nums, target));
