/**
 * 
 * PalindromePartition.java
 * Mar 23, 2013
 */
import java.util.ArrayList;
/**
 * @author huangsp
 *
 */
public class PalindromePartition {
	public int palindromePartition(String input){
		int count = 0;
		int len = input.length();
		int start = 0, end = len - 1;
		String substring = "";
		while(end > start){
			substring = input.substring(start, end + 1);
			while(!check(substring)){
				end --;
				substring = input.substring(start, end + 1);
			}
			if (end != len - 1)		count ++;
			start = end + 1;
			end = len - 1;
		}
		return count;
	}
	private boolean check(String input){
		int start = 0;
		int end = input.length() - 1;
		while(start < end){
			if (input.charAt(start) != input.charAt(end))	return false;
			else{
				start ++;
				end --;
			}
		}
		return true;
	}
	public ArrayList<ArrayList<String>> partition(String s) {
	    if(s == null || s.length() == 0)
	        return new ArrayList<ArrayList<String>>();
	    boolean[][] isPalindrome = new boolean[s.length()][s.length()];
	    for(int i = 0; i < s.length(); i++){
	        isPalindrome[i][i] = true;
	    }
	    for(int i = s.length() - 2; i >= 0; i --){
	        isPalindrome[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));
	        for(int j = i + 2; j < s.length(); j++) 
	            isPalindrome[i][j] = (s.charAt(i) == s.charAt(j)) && isPalindrome[i + 1][j - 1];
	    }
	    return partition(s, 0, isPalindrome);
	}

	private ArrayList<ArrayList<String>> partition(String s, int start, boolean[][] isPalindrome){
	    ArrayList<ArrayList<String>> partitionList = new ArrayList<ArrayList<String>>();
	    if(start == s.length()){
	        partitionList.add(new ArrayList<String>());
	        return partitionList;
	    }
	    for(int i = start; i < s.length(); i++){
	        if(isPalindrome[start][i])
	            for(ArrayList<String> subPartitionList: partition(s, i + 1, isPalindrome)){
	                subPartitionList.add(0, s.substring(start, i + 1));
	                partitionList.add(subPartitionList);
	            }
	    }
	    return partitionList;
	}
	public static void main(String[] args){
		PalindromePartition myTest = new PalindromePartition();
		System.out.println(myTest.palindromePartition("aabcbaa"));
		System.out.println(myTest.partition("aabaa"));
	}
}
