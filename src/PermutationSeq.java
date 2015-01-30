import java.util.ArrayList;

/**
 * 
 * PermutationSeq.java
 * Nov 29, 2012
 */

/**
 * @author Shubo Liu
 *	O(n) time and O(1) space
 */
public class PermutationSeq {
	public String getPermutation(int n, int k) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if ( k > factorial(n) || k < 1) return "";
        else if (n == 1)	return "1";
        else{
        	StringBuffer out = new StringBuffer();
        	boolean[] used = new boolean[n];
        	return getPermutation(n, k-1, used, out).substring(0,n);
        }
    }
	private String getPermutation(int n, int k, boolean[] used, StringBuffer out){
        if (n == 1)	{
        	int m = 0;
        	while(used[m]) m++;
        	return m+1+"";
        }
        else{
        	int m = k / factorial(n - 1) + 1;
        	int index = 0;
        	while( m > 0){
        		if (!used[index]) m--;
        		index++;
        	}
        	index--;
        	used[index] = true;
        	out.append(index + 1 + "");
        	k %= factorial(n - 1);
        	out.append(getPermutation(n-1, k, used, out));
        	return out.toString();
        }
	}
	
	public String permutation(int n, int k){
		if ( k > factorial(n) || k < 1) return "";
        else if (n == 1)	return "1";
        else{
        	StringBuffer out = new StringBuffer();
        	ArrayList<Integer> candidates = new ArrayList<Integer>();
        	for (int index = 1; index <= n; index++){
        		candidates.add(index);
        	}
        	return permutation(n, k-1, candidates, out).substring(0,n);
        }
	}
	private String permutation(int n, int k, ArrayList<Integer> candidates, StringBuffer out){
		if (candidates.size() == 1){
			int digit = candidates.remove(0);
			out.append(digit + "");
		}else{
			int m = k / factorial(n - 1);
			int digit = candidates.remove(m);
			out.append(digit + "");
			k %= factorial(n-1);
			permutation(n-1, k, candidates, out);
		}
		return out.toString();
	}
	
	private int factorial(int n){
		if (n == 1) return 1;
		else
			return n * factorial(n - 1);
	}
	
	public static void main(String[] args){
		System.out.println(new PermutationSeq().getPermutation(9, 37));
		System.out.println(new PermutationSeq().permutation(9, 37));

	}
}
