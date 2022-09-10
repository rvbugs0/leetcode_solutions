class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        complement ={}
        complement["}"] = "{"
        complement[")"] ="("
        complement["]"] = "["
        for c in s:

            if c in ['{','[','(']:

                stack.append(c)

            else:

                stack_size = len(stack)

                if(stack_size!=0 and stack[stack_size-1]==complement[c] ):

                    stack.pop()

                else:

                    return False

           

        

        if(len(stack)==0): return True

        return False