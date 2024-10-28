class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_num = min(nums)
        max_num = max(nums)
        
        # Special case: if all numbers are the same
        if min_num == max_num:
            return 0
        
        n = len(nums)
        bucket_size = max(1, (max_num - min_num) // (n - 1))  # Minimum size of 1
        bucket_count = (max_num - min_num) // bucket_size + 1
        
        # Create buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Place numbers into buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)  # Update min in the bucket
            buckets[idx][1] = max(buckets[idx][1], num)  # Update max in the bucket
            
        # Calculate the maximum gap
        max_gap = 0
        previous_max = min_num
        
        for bucket in buckets:
            if bucket[0] == float('inf'):
                continue  # Skip empty buckets
            # The gap is between the previous maximum and the current bucket minimum
            max_gap = max(max_gap, bucket[0] - previous_max)
            previous_max = bucket[1]  # Update previous maximum to the current bucket's max
        
        return max_gap

# Example usage:
# sol = Solution()
# print(sol.maximumGap([3, 6, 9, 1]))  # Output: 3
# print(sol.maximumGap([10]))           # Output: 0
