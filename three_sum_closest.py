class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        zeroCount = 0
        newArr = []
        for i in range (len(nums)):
            if nums[i]!=0:
                newArr.append(nums[i])
            else:
                zeroCount+=1

        while(zeroCount!= 0 and zeroCount<=3):
            newArr.append(0)
            zeroCount-=1

        newArr.sort()
        i = 0
        closest = 100000000000000
        while(i<len(newArr)):

            currElement = newArr[i]
            del newArr[i]
            newArr.insert(0,currElement)

            start = 1
            end = len(newArr)-1
            while(start<end):
                s = newArr[start]+newArr[end]+newArr[0]
                if(s==target):
                    return s
                elif (s>target):
                    if(abs(target-s)<abs(target-closest)):
                        closest = s
                    end-=1
                else:
                    if(abs(target-s)<abs(target-closest)):
                        closest = s
                    start+=1
            del newArr[0]
            newArr.insert(i,currElement)
            i+=1
        return closest

