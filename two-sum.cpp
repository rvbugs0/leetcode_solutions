class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> sortedArrayWithIndices;
        for(int i=0;i<nums.size();i++)
        {
            sortedArrayWithIndices.push_back(pair<int,int>(nums[i],i));
        }
        vector<int> result; 
        sort(sortedArrayWithIndices.begin(),sortedArrayWithIndices.end());
        int i=0;
        int j=nums.size()-1;
        while(i<j)
        {
            if(sortedArrayWithIndices[i].first+ sortedArrayWithIndices[j].first==target)
            {
                result.push_back(sortedArrayWithIndices[i].second);
                result.push_back(sortedArrayWithIndices[j].second);
                break;
                
            }else if(sortedArrayWithIndices[i].first+ sortedArrayWithIndices[j].first<target)
            {
                i++;
            }else // when sum is more than target, we reduce j
            {
                j--;
            }
        }
        
        
        return result;
            
            
    }
};