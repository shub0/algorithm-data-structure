import java.util.Arrays;

/**
 * 
 * NextPermutation.java
 * Nov 28, 2012
 */

/**
 * @author Shubo Liu
 * O(n) time and O(1) space
 *
 */
public class NextPermutation {
	public void nextPermutation(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = num.length;
        if (len < 2) return;
        else{
            int index = len - 1;
            int max = num[index];
            for (; index >= 0; index--){
                if (max > num[index]){
                    break;
                }
                max = num[index];
            }
            reverse(num, index + 1, len - 1);
            if (index == -1) return;
            else{
                for (int i = index + 1; i < len; i++){
                    if (num[i] > num[index]){
                        swap(num, i, index);
                        break;
                    }
                }  
            }
        }
    }
	public void previousPermutation(int[] num){
		int len = num.length;
		if (len < 2)	return;
		else{
			int index = len - 1;
			int min = num[index];
			for (; index >= 0; index --){
				if (min < num[index]){
					break;
				}else{
					min = num[index];
				}
			}
			reverse(num, index + 1, len - 1);
			if (index == -1)	return;
			else{
				for (int i = index + 1; i < len; i++){
					if (num[i] < num[index]){
						swap(num, i, index);
						break;
					}
				}
			}
		}
	}
    private void reverse(int[] num, int startPos, int endPos){
        while (startPos < endPos){
            swap(num, startPos, endPos);
            endPos -- ;
            startPos ++;
        }
    }
    private void swap(int[] num, int index1, int index2){
        int tmp = num[index1];
        num[index1] = num[index2];
        num[index2] = tmp;
    }
    public static void main(String[] args){
    	int[] num = {2,6,5,4,3,1};
    	new NextPermutation().previousPermutation(num);
    	System.out.println(Arrays.toString(num));
    }
}
