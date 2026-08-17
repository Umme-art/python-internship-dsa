class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int cur = gas[0] - cost[0];
        int mini = cur;
        int index = 0;
        for (int i = 1; i < gas.size(); i++) {
            cur += gas[i] - cost[i];
            if (cur < mini) {
                mini = cur;
                index = i;
            }
        }
        if (cur < 0) {
            return -1;
        }
        return (index + 1) % gas.size();
    }
};