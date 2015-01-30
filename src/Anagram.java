/**
 * 
 * Anagram.java
 * Nov 22, 2012
 */
import java.util.*;
/**
 * @author Shubo Liu
 *
 */
public class Anagram {
	 public ArrayList<String> anagrams(String[] strs) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
		 	// O(N^2) time complexity
	        ArrayList<String> list = new ArrayList<String>();
	        if (strs.length < 2) return list;
	        else{
	            int size = strs.length;
	            boolean[] visited = new boolean[size];
	            for (int index1 = 0; index1 < size; index1++){
	                if (visited[index1]) continue;
	                visited[index1] = true;
	                boolean flag = false;
	                for (int index2 = 0; index2 < size; index2++){
	                    if (visited[index2])  continue;
	                    if (check(strs[index1],strs[index2])){
	                        flag = true;
	                        list.add(strs[index2]);
	                        visited[index2] = true;
	                    }
	                }
	                if (flag) list.add(strs[index1]);
	            }
	        }
	        return list;
	    }
	     private boolean check(String thisStr, String thatStr){
	    	 	
	        	if (thisStr.length() != thatStr.length()) return false;
	        	int[] freq = new int[26];
		        char[] thisArray = thisStr.toCharArray();
		        char[] thatArray = thatStr.toCharArray();
		        int len = thisStr.length();
		        for (int index = 0; index < len; index++){
		            freq[thisArray[index] - 'a']++;
		        }
		        for (int index = 0; index < len; index++){
		            freq[thatArray[index] - 'a']--;
		        }
		        for (int index = 0; index < 26; index++){
		        	if (freq[index] != 0) return false;
		        }
		        return true;
		    }
	     public static void main(String[] args){
	    	 String[] strs = {"hos","jew","nub","cod","old","way","fur","fla","cot","baa","leo","uzi",
	    			 "tho","pry","tun","hex","fog","tad","eat","sow","cop","eke",
	    			 "jam","arc","guy","tow","aid","ann","bus","ten","ate","ewe","roy","leg","gas","bug","jay","sup","phd"};
	    	 System.out.println(new Anagram().anagrams(strs));
	     }
}
