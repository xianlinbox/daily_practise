from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(0, len(gas)):
            remain_gas = gas[i]
            remain_gas -= cost[i]
