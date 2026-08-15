class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

// TO find the row in which our element present
        int m = matrix.length;int n = matrix[0].length;
        int low =0;int high = m-1;
        int row = -1;
        while(low<=high){
            int mid = low + (high-low)/2;
            if(matrix[mid][n-1]==target) return true;
            else if(matrix[mid][n-1]<target){
                low = mid+1;
            }
               
            else{
                 row = mid;
                 high=mid-1;
            }
        }
// if the element is lower than all elements in matrix return -1;
        if(row==-1) return false;

// applying binary search on the row which we Found
        int l = 0;int h = n-1;
        while(l<=h){
            int midd = l + (h-l)/2;
            if(matrix[row][midd]==target) return true;
            else if(matrix[row][midd]<target){
                l = midd+1;
            }else{
                h = midd-1;
            }
        }
        return false;

    }
}