from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station_count = len(gas)
        current_index = 0
        while current_index < station_count:
            remain_gas = gas[current_index] - cost[current_index]
            j = current_index + 1
            while remain_gas >= 0:
                remain_station_index = j % station_count
                remain_gas += gas[remain_station_index] - cost[remain_station_index]
                if remain_station_index == current_index:
                    return current_index
                j += 1
            remain_gas = 0
            current_index = j
        return -1
