/**
 * 
 * JumpGame.java
 * Nov 26, 2012
 */

/**
 * @author huangsp
 *
 */
public class JumpGame {
	public boolean canJump(int[] A){
		if (A.length < 2) return true;
		else{
			int max = 0;
			for (int index = 0; index < A.length; index++){
				int tmp = index + A[index];
				if (tmp > max){
					max = tmp;
				}
				if (max >= A.length - 1)
					break;
				if (index == max){
					return false;
				}
			}
			return true;
		}
	}
	public int jump(int[] A){
		if (A.length < 2) return 0;
		else{
			int len = A.length;
			int max = 0;
			// dynamic programming
			int[] minMove = new int[len];
			minMove[0] = 0;
			for (int index = 0; index < len; index++){
				int tmp = index + A[index];
				if (tmp > max){
					for (int index2 = max+1; index2 <= Math.min(tmp, len - 1); index2++){
						minMove[index2] = minMove[index] + 1;
					}
					max = tmp;
				}
				if (max >= len - 1)
					break;
				//cannot arrive last position
				if (index == max){
					return Integer.MAX_VALUE;
				}
			}
			return minMove[len - 1];
		}
	}
	public static void main(String[] args){
		int[] A = {5,9,3,2,1,0,2,3,3,1,0,0};
			System.out.println(new JumpGame().jump(A));
	}
}
