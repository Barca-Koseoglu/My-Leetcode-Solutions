class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Make a list called record. Then loop through operations. If changing the current iteration to an integer makes an error use try and except for the 
        other operations. Then return the sum of record.
        """
        record = []
        for i in operations:
            try:
                record.append(int(i))
            except:
                if i == "C":
                    record.pop()
                elif i == "D":
                    record.append(record[-1]*2)
                else:
                    record.append(record[-1]+record[-2])
        return sum(record)
