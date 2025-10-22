class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_int = 0
        for i in operations:
            if "++" in i:
                final_int += 1
            else:
                final_int -= 1
        
        return final_int
