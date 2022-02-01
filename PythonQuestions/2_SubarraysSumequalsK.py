from collections import defaultdict
def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        sums = defaultdict(int)
        print(sums)
        running_sum = 0
        
        for num in nums:
            print(num)
            running_sum += num
            print(running_sum)
            if running_sum == k:
                total+=1
                break
            if running_sum - k in sums:
                print(sums[running_sum - k])
                total += sums[running_sum - k]
            
            sums[running_sum] +=1
            print(sums)
        print(total)
nums = [1,2,3,2,4] 
k = 4      
subarraySum(nums,k)