from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain_gas = 0
        station_count = len(gas)
        for i in range(0, station_count):
            remain_gas = gas[i] - cost[i]
            j = i
            while remain_gas >= 0:
                j = (j + 1) % station_count
                remain_gas += gas[j] - cost[j]
                if j == i:
                    return i

        return -1
