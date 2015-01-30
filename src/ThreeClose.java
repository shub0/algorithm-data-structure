/**
 * 
 * ThreeClose.java
 * Nov 22, 2012
 */
import java.util.*;
/**
 * @author huangsp
 *
 */
public class ThreeClose {
	public int threeSumClosest(int[] num, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Arrays.sort(num);
        int len = num.length;
        int bestSum = Integer.MAX_VALUE;
        for (int index = 0; index < len - 2; index++){
            int left = index + 1;
            int right = len - 1;
            
            while ( left < right){
                int sum = num[index] + num[left] + num[right] - target;
                if (abs(bestSum) > abs(sum))
                    bestSum = sum;
                if (sum > 0) right -- ;
                else if(sum < 0) left ++;
                else break;
            }
        }
        return bestSum + target;
    }
    public int abs(int a){
        if (a > 0) return a;
        else return -a;
    }
    public static void main(String[] args){
    	int[] data = {1,1,1,0};
    	System.out.println(new ThreeClose().threeSumClosest(data, 100));
    }
}
