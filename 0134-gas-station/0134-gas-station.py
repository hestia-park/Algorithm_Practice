class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        minval = 1e9
        minpos = -1
        current_gas=0
        for i in range(len(gas)):
            current_gas+=gas[i]-cost[i]
            if current_gas < minval:
                minval = current_gas
                minpos = i
                print(i,minval,minpos)
        if current_gas >= 0:
            return (minpos+1) % len(gas)
        return -1       