class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        // If the target is greater than the sum of both jugs, it's impossible.
        if (x + y < target) {
            return false;
        }

        // Handle edge cases where one or both jugs are 0
        if (x == 0) {
            return target == y || target == 0;
        }
        if (y == 0) {
            return target == x || target == 0;
        }

        while (x != 0) {
            int temp = x;
            x = y % x;
            y = temp;
        }

        return target % y == 0;
    }
}