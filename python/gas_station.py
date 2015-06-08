#! /usr/bin/python

'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
'''

'''
Alg here:
Greedy algorithm, try to carry as much gas as possible. Therefore the problem is transferred to a max-sum subarray problem
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) != len(cost) or len(gas) == 0 or sum(gas) < sum(cost):
            return -1
        total_station = len(gas)
        gas_in_tank = 0
        start_station = 0
        for station in range(0, total_station):
            gas_in_tank += gas[station]
            gas_in_tank -= cost[station]
            if gas_in_tank < 0:
                gas_in_tank = 0
                start_station = station + 1
        return start_station

if __name__ == '__main__':
    solution = Solution()
    print solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
