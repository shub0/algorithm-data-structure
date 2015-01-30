/**
 * 
 * RainWater.java
 * Dec 11, 2012
 */

/**
 * @author huangsp
 *
 */
public class RainWater {
	public int trap(int[] A){
		int len = A.length;
		if (len == 0)	return 0;
		else{
			int[] left = new int[len];
			int[] right = new int[len];
			int maxHeight = 0;
			for(int index = 0; index < len; index++){
				left[index] = maxHeight;
				maxHeight = Math.max(A[index], maxHeight);
			}
			maxHeight = 0;
			for (int index = len - 1; index >= 0; index--){
				right[index] = maxHeight;
				maxHeight = Math.max(A[index], maxHeight);
			}
			int sum = 0;
			for (int index = 0; index < len; index++){
				int tmp = Math.min(left[index], right[index]) - A[index];
				if (tmp > 0)	sum += tmp;
			}
			return sum;
		}
	}
	public static void main(String[] args){
		int[] A = {0,1,0,2,1,0,1,3,2,1,2,1};
		System.out.println(new RainWater().trap(A));
	}
}
