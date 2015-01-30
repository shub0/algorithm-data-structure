/**
 * 
 * Median.java
 * Nov 27, 2012
 */

/**
 * @author huangsp
 *
 */
public class Median {
	double findMedian(int[] A, int[] B){
		int len = A.length + B.length;
		if (len % 2 ==0){
			return (double) findKth(A, 0, A.length, B, 0, B.length, len /2) * 0.5 
					+ (double) findKth(A, 0, A.length, B, 0, B.length, len /2 + 1)  * 0.5;
		}
		else return findKth(A, 0, A.length, B, 0, B.length, len /2 + 1);
	}
	int findKth(int[] A, int offsetA, int m, int[] B, int offsetB, int n, int k){
		if (m > n) 	return findKth(B, offsetB, n, A, offsetA, m, k);
		if (m == 0) return B[k-1];
		if (k == 1) return Math.min(A[offsetA], B[offsetB]);
		int pa = Math.min(k/2, m);
		int pb = k - pa;
		if (A[offsetA + pa - 1] < B[offsetB + pb - 1]) return findKth(A, offsetA + pa, m - pa, B, offsetB, n, k - pa);
		else return findKth(A, offsetA, m, B, offsetB + pb, n - pb, k - pb);
	}
	public static void main(String[] args){
		int[] A = {1,2,3,4,5};
		int[] B = {2,4,6};
		System.out.println(new Median().findMedian(A, B));
	}
}
