/**
 * 
 * IntervalString.java
 * Nov 26, 2012
 */

/**
 * @author Shubo Liu
 *
 */
public class IntervalString {
	 public boolean isInterleave(String s1, String s2, String s3){
		 int len1 = s1.length();
		 int len2 = s2.length();
		 int len3 = s3.length();
		 if (len1 + len2 != len3)	return false;
		 return isInterleave(s1, len1, s2, len2, s3, len3);
	 }
	 private boolean isInterleave(String s1, int len1, String s2, int len2, String s3, int len3){
		 if (len3 == 0)	return true;
		 else{
			 // s1 first search
			 boolean  first = (len1 > 0) && (s1.charAt(len1 - 1) == s3.charAt(len3 - 1))
					 && isInterleave(s1, len1 - 1, s2, len2, s3, len3 - 1);
			 // s2 first search
			 boolean second = (len2 > 0) && (s2.charAt(len2 - 1) == s3.charAt(len3 - 1))
					 && isInterleave(s1, len1, s2, len2 - 1, s3, len3 - 1);
			 return first || second;
		 }
	 }
	 public static void main(String[] args){
		 String s3 = "aaba";
		 String s2 = "ab";
		 String s1 = "aa";
		 System.out.println(new IntervalString().isInterleave(s1, s2, s3));
	 }
}
