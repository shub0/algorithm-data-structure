/**
 * 
 * SortColor.java
 * Dec 12, 2012
 */

/**
 * @author huangsp
 *
 */
public class SortColor {
	public void sortColors(int[] A) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = A.length;
        if (len == 0) return;
        else{
            int left = 0; 
            int right = len - 1;
            int current = 0;
            while(left <= right && current <= right){
                while ( left <= right && A[left] == 0){
                    left++;
                }
                while ( left <= right && A[right] == 2){
                    right --;
                }
                current = left;
                while ( current <= right && A[current] == 1){
                    current ++;
                }
                if(left <= right && current <= right){
                    if (A[current] == 0)    swap(A, left, current);
                    else    swap(A,current, right);
                }
            }
        }
    }
    private void swap(int[] A, int src, int dest){
        int tmp = A[src];
        A[src] = A[dest];
        A[dest] = tmp;
    }
}
