from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain_gas = 0
        for i in range(0, len(gas)):
            remain_gas = gas[i] - cost[i]
            j = i
            while remain_gas > 0:
                print(i, j)
                j += 1
                remain_gas += gas[j % len(gas)] - cost[j % len(gas)]
                if j == i:
                    return i

        return -1
