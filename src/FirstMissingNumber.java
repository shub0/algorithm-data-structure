/**
 * 
 * FirstMissingNumber.java
 * Nov 26, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class FirstMissingNumber {
	 public int firstMissingPositive(int[] A){
		 int len = A.length;
		 if (len == 0) 	return 1;
		 else{
			int index = 0;
			for (;index < len; index++){
				while (A[index] != index + 1){
					if (A[index] != index + 1 && A[index] <= len && A[index] > 0 && A[index] != A[A[index] - 1])
						swap(A, index, A[index] - 1);
					else break;
				}
			 }
			 index = 0;
			 for (index = 0; index < len; index++){
				 if (A[index] != index + 1)
					 break;
			 }
			 return index + 1;
			 /*
			 if (index == len - 1 && A[index] == len)
				 return len + 1;
			 else
				 return index + 1;
				 */
		 }
	}
	 private void swap(int[] A, int index1, int index2){
		 int tmp = A[index1];
		 A[index1] = A[index2];
		 A[index2] = tmp;
	 }
	 public static void main(String[] args){
		 int[] data = {2,4,5,6,1,7,3};
 		 System.out.println(new FirstMissingNumber().firstMissingPositive(data));
	 }
}
