/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    var avg = -1000000;
    var windowEnd = 0;
    windowStart = 0;
    var windowSum = 0;
    while(windowEnd<nums.length)
        {
            windowSum+=nums[windowEnd];
            if(windowEnd>=k-1)
                {
                    avg = Math.max(avg, windowSum/k);
                    windowSum = windowSum - nums[windowStart++];
                }
            
            windowEnd+=1;
        }
        return avg;
    }