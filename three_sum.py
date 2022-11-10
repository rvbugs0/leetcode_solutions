class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map_val ={}

        map_newarr= {}
        newArr =[]
        zeroCount = 0
        for i in range (len(nums)):
                if(nums[i]!=0):
                    newArr.append([nums[i],i])
                else:
                    zeroCount+=1

        if(zeroCount>=3):
            for i in range(3):
                newArr.append([0,len(newArr)])
        elif(zeroCount!=0):
            for i in range(zeroCount):
                newArr.append([0,len(newArr)])

        
        
        newArr.sort()
        
        if(len(newArr)<3):
            return []
        # print(newArr)
        # print("---------------------")
        triplets = []
        #replace first element with first, second and so on
        i=0

        while(i<len(newArr)):
            currElement = newArr[i]
            del newArr[i]
            newArr.insert(0,currElement)

            # print("new arr: ",newArr)
            #swapped first element with ith element
            # print("Swapped arr: ",newArr)
            start  = 1
            end = len(newArr)-1

            while(start<end):
                
                # print("Target is ",target)
                s = (newArr[start][0]+ newArr[end][0])+ newArr[0][0]
                if (s==0):
                    tpt = [newArr[start][0], newArr[end][0], newArr[0][0]]

                    tpt.sort()
                    st = str(tpt[0])+"-"+str(tpt[1])+"-"+str(tpt[2])
                    # print(tpt)
                    if st not in map_val:
                        map_val[st]=1
                        triplets.append(tpt)
                    start+=1                    
                    # break    

                elif(s<0):
                    start+=1
                else:
                    end-=1


            del newArr[0]
            newArr.insert(i,currElement)
            i+=1

        return triplets

        
        
        