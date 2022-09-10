/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
   
    sorted_strings= strs.sort((a,b)=> (a.length-b.length));
   
    first_string = strs[0];
   
    prefix = "";
   
    for(x=0;x<first_string.length;x++)
    {
        completeCycle=true;
        for(y=1;y<strs.length;y++)
            {
                if(strs[y][x]!=first_string[x])
                    {
                        completeCycle=false;
                        break;
                    }
               
            }
        if(completeCycle){
            prefix+=first_string[x];
        }else
            {
                break;
            }
       
       
    }
   
    return prefix;
   
   
   
   
   
   
   
};