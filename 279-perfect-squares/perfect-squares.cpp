class Solution {
public:

    bool isPerfectSquare(int n) {
        int root = sqrt(n);
        return root * root == n;
    }

    int numSquares(int n) {

        // Case 1: n itself is a square
        if(isPerfectSquare(n))
            return 1;

        // Case 2: n = a² + b²
        for(int i = 1; i * i <= n; i++) {

            if(isPerfectSquare(n - i * i))
                return 2;
        }

        // Case 4: n = (4^a) * (8b + 7)
        while(n % 4 == 0)
            n /= 4;

        if(n % 8 == 7)
            return 4;

        // Otherwise, answer must be 3
        return 3;
    }
};