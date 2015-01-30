/**
 * 
 * PalindromeNumber.java
 * Nov 29, 2012
 */

/**
 * @author huangsp
 *
 */
public class PalindromeNumber {
	 public boolean isPalindrome(int x) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        int highBase = 1;
	        while ( x / highBase > 9){
	            highBase *= 10;
	        }
	        while ( highBase > 1){
	            int highDigit = x / highBase;
	            int lowDigit = x % 10;
	            if (highDigit != lowDigit){
	                return false;
	            }
	            x %= highBase;
	            x /= 10;
	            highBase /= 100;
	        }
	        return true;
	    }
	 public static void main(String[] args){
		 System.out.println(new PalindromeNumber().isPalindrome(121));
	 }
}
