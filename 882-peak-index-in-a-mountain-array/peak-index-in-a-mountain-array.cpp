class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int n=arr.size();
        int low=1;
        int high=n-2;
        int mid=0;
        int peak=0;
        while(low<=high){
            mid=(low+high)/2;
            if(arr[mid]>=arr[mid-1]){
                peak=mid;
                low=mid+1;
            }
            else if(arr[mid]<arr[mid-1]){
                high=mid-1;
            }
        }
        return peak;
    }
};