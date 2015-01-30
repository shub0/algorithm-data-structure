import java.util.Arrays;

/**
 * 
 * RemoveDuplicate.java
 * Dec 3, 2012
 */

/**
 * @author huangsp
 * Another two versions of link list duplicates removal algorithm are in DataStrucutre package
 */
public class RemoveDuplicate {
	public int removeDuplicateSingle(int[] num){
		if (num.length < 2) return num.length;
		else{
			int distinctLen = 1;
			for (int index = 1; index < num.length; index++){
				if (num[index] != num[index - 1]){
					num[distinctLen++] = num[index];
				}
			}
			return distinctLen;
		}
	}
	public int removeDuplicateSingle2(int[] num) {
		int len = num.length;
		if (len < 2)    return len;
		else{
			int newLen = 0;
			for (int index = 1; index < len; index++){
				if (num[index] != num[newLen]){
					num[ ++newLen] = num[index];
	            }
			}
	        return ++newLen;
	    }
	}

	public int removeDuplicateDobule(int[] num){
		if (num.length < 3) return num.length;
		else{
			int distinctLen = 1;
			boolean flag = false;
			for (int index = 1; index < num.length; index++){
				if (num[index] != num[index - 1]){
					num[distinctLen++] = num[index];
					flag = false;
				}else{
					if (!flag){
						flag = true;
						num[distinctLen++] = num[index];
					}
				}
			}
			return distinctLen;
		}
	}
	// more elegant than removeDuplicateDouble algorithm by removing flag
	public int removeDuplicateDouble2(int[] num){
		if (num.length < 3)	return num.length;
		else{
			int newLen = 1;
			for (int index = 2; index < num.length; index++){
				if (num[index] == num[newLen] && num[index] == num[newLen - 1]){
					continue;
				}
				num[++newLen] = num[index];
			}
			return ++newLen;
		}
	}
	public int removeInstance(int num[], int removeData){
		int len = 0; 
		for (int index = 0; index < num.length; index++){
			if (num[index] != removeData){
				num[len++] = num[index];
			}
		}/*
		for (int index = len; index < num.length; index++){
			num[index] = Integer.MIN_VALUE;
		}*/
		return len;
	}
	public static void main(String[] args){
		int[] num = {1,1,1,1,2,2,3,3,3,4};
		RemoveDuplicate myProblem = new RemoveDuplicate();
		int len = myProblem.removeDuplicateDouble2(num);
		System.out.println(len);
		System.out.println(Arrays.toString(num));	
	}
	
}
