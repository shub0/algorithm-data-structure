import java.util.Arrays;

/**
 * 
 * Merge.java
 * Nov 28, 2012
 */

/**
 * @author huangsp
 *
 */
public class Merge {
	 public static void merge(int A[], int m, int B[], int n){
		 if (n == 0) return;
	        if (m == 0) 
	        {
	           for (int index = 0; index < n; index++)
	               A[index] = B[index];
	        } 
	        int index = m + n - 1;
	        int indexA = m - 1;
	        int indexB = n - 1;
	        while (indexA >= 0 && indexB >= 0){
	            if (A[indexA] > B[indexB]){
	                A[index--] = A[indexA--];
	            }else{
	                A[index--] = B[indexB--];
	            }
	        }
	        if (indexA < 0){
	            while (indexB >= 0)
	                A[index--] = B[indexB--];
	        }else{
	            while(indexA >= 0)
	                A[index--] = A[indexA--];
	        }
	 }
	 public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		 ListNode head = new ListNode(0);
		 ListNode current = head;
		 while (l1 != null && l2 != null){
			 if (l1.val > l2.val) {
				 current.next = l1;
				 l1 = l1.next;
			 }
			 else{
				 current.next = l2;
				 l2 = l2.next;
			 }
			 current = current.next;
		 }
		 if (l1 == null){
			 current.next = l2;
		 }else{
			current.next = l1;
		 }
		 return head.next;
	 }
	 public static void main(String[] args){
		 int[] A = new int[5];
		 A[0] = 4;
		 A[1] = 5;
		 int[] B = {1,2,3};
		 merge(A, 2, B,3);
		 System.out.println(Arrays.toString(A));
	 }
}
